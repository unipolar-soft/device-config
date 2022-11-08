# This Python file uses the following encoding: utf-8
import logging
from logging.config import dictConfig
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow,QInputDialog
from PySide6.QtGui import QIntValidator
from .ui.ui_mainwindow import Ui_MainWindow
from .projutil.log_conf import DIC_LOGGING_CONFIG
from .projutil.conf import LOGGER_NAME
from .ui.ui_mainwindow import Ui_MainWindow
from .projutil.log_conf import DIC_LOGGING_CONFIG
from .projutil.conf import LOGGER_NAME
import serial.tools.list_ports as port_list
from app.ui.serial_port import SerialPort


dictConfig(DIC_LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)

# Here is a mapping from device type to device model
type_to_model = {
    "2 CH AI,4 Ch DI" : "01",
    "4 CH AI" : "02",
    "8 CH DO" : "03"
}
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        validator = QIntValidator(1,147, self)                      # Validate slave Id filed
        self.input = self.ui.slaveIdInput.setValidator(validator)

        self.ui.actionConnect.triggered.connect(self.port_selection)
        
        self.ui.findDevice.clicked.connect(self.find_device)

        self.ui.configure.clicked.connect(self.configure)

        self.ui.modelNoInput.setText(type_to_model[self.ui.typeInput.currentText()])               # map the device type to model

        self.thread = SerialPort()                                  # Instantiate the SeraialPort class.
        self.thread.feedback.connect(self.receive_fb)

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
# This function's main purpose is to send the find message to the thread as well as display the current field's data on the text field.
    def find_device(self):
        config = {
            "COM_port" : self.ui.comportinput.text(),
            "device" : self.ui.comboBox.currentText(),
            "d_type" : self.ui.typeInput.currentText(),
            "model_no" : type_to_model[self.ui.typeInput.currentText()],
            "slave_id" : self.ui.slaveIdInput.text(),
            "baud_rate" : self.ui.baudRateInput.currentText(),
            "parity" : self.ui.parityInput.currentText()
        }
        find_message = "UNP\rFND\r\n"
        feedback = "UNP\rACK:1\rMDN:01\rSLN:12345\rSID:101\rBDR:1\rPRB:0\r\n"
        self.ui.listWidget.clear()
        for key, value in config.items():
            try:
                print(key+" : "+value)
                self.ui.listWidget.addItem( key +" : "+value)
            except:
                print("Data is not printing in the text box")   
        self.thread.send_data(find_message)

    def select_port(self):
        port_name = self.ui.comPortInput.currentText()[0:4]
        self.serial_port.port = port_name
# This function is used for receving the feedback from the thread which is comming from device.
    def receive_fb(self,fb):
        splitted_string = fb.split("\r")
        if "\n" and "UNP" in fb:
            print("true")
            splitted_string.remove("\n")
            splitted_string.remove("UNP")
        config_dic = {}
        for item in splitted_string:
            splited_item = item.split(":")
            config_dic[splited_item[0]] = splited_item[1]
        print(config_dic)
        if "SLN" in config_dic.keys():
            self.ui.serialNoInput.setText(config_dic['SLN'])
        if "SID" in config_dic.keys():    
            self.ui.slaveIdInput.setText(config_dic['SID'])
        if "BDR" in config_dic.keys():    
            self.ui.baudRateInput.setCurrentIndex(int(config_dic['BDR']))
        if "PRB" in config_dic.keys():
            self.ui.parityInput.setCurrentIndex(int(config_dic['PRB']))
        self.ui.listWidget.clear()
        for key, value in config_dic.items():
            try:
                print(key+" : "+value)
                self.ui.listWidget.addItem( key +" : "+value)
            except:
                print("Data is not printing in the text box") 
# This function is used for sending the user selected configuration to the thread
    def configure(self):
        configure_info = "UNP\rCFG\rMDN:"+type_to_model[self.ui.typeInput.currentText()]+"\rSID:"+self.ui.slaveIdInput.text()+"\rBDR:"+str(self.ui.baudRateInput.currentIndex())+"\rPRB:"+str(self.ui.parityInput.currentIndex())+"\r\n"
        self.thread.send_data(configure_info)
# This function displays the available COM port and then start the thread. 
    def port_selection(self):
        ports = list(port_list.comports())                           # Here is the available COM port list
        port_name_list = []
        for port in ports:
            port_name_list.append(port.name+"-"+port.description)
        item, ok = QInputDialog.getItem(self, "Select COM Port",
                                "Port:", port_name_list, 0, False)   # This dialog box diaplay the COM port list
        if ok and item:
           self.ui.comportinput.setText(item)
           self.thread.port_setup(item[0:4])                         # Here send the selected COM port to the thread 
           self.thread.start()                                 