# This Python file uses the following encoding: utf-8
from cgi import test
from concurrent.futures import thread
from email import message
import os
from pathlib import Path
from select import select
import sys
import logging
from logging.config import dictConfig
import PySide6

from PySide6.QtWidgets import QMainWindow,QListWidgetItem
from PySide6.QtCore import Qt,Signal, Slot
from PySide6.QtGui import QIntValidator
from .ui.ui_mainwindow import Ui_MainWindow
from .projutil.log_conf import DIC_LOGGING_CONFIG
from .projutil.conf import LOGGER_NAME
from .ui.ui_mainwindow import Ui_MainWindow
from .projutil.log_conf import DIC_LOGGING_CONFIG
from .projutil.conf import LOGGER_NAME
import serial.tools.list_ports as port_list
import serial
import time
from app.ui.serial_port import SerialPort

dictConfig(DIC_LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)
type_to_model = {
    "2 CH AI,4 Ch DI" : "01",
    "4 CH AI" : "02",
    "8 CH DO" : "03"
}
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        self.thread = SerialPort()
        # self.thread.started.connect(self.feedback)
        self.thread.start()
        # Validate slave Id filed 
        validator = QIntValidator(1,147, self)
        self.input = self.ui.slaveIdInput.setValidator(validator)

        self.ui.findDevice.clicked.connect(self.find_device)

        self.ui.configure.clicked.connect(self.configure)

        self.ui.typeInput.currentTextChanged.connect(self.test)
        # map the device type to model
        self.ui.modelNoInput.setText(type_to_model[self.ui.typeInput.currentText()])
        
        self.thread.feedback.connect(self.receive_fb)
        # list the comunication port
        ports = list(port_list.comports())
        for i,p in enumerate(ports):
            self.ui.comPortInput.insertItem(i,p.name+"-"+p.description)  # Display the port in combobox 

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def find_device(self):
        config = {
            "COM_port" : self.ui.comPortInput.currentText(),
            "device" : self.ui.comboBox.currentText(),
            "d_type" : self.ui.typeInput.currentText(),
            "model_no" : type_to_model[self.ui.typeInput.currentText()],
            "slave_id" : self.ui.slaveIdInput.text(),
            "baud_rate" : self.ui.baudRateInput.currentText(),
            "parity" : self.ui.parityInput.currentText()
        }
        print(config)
        find_message = "UNP\rFND\r\n"
        # feedback = "UNP\rACK:1\rMDN:01\rSLN:12345\rSID:101\rBDR:1\rPRB:0\r\n"
        self.ui.listWidget.clear()
        for key, value in config.items():
            try:
                print(key+" : "+value)
                self.ui.listWidget.addItem( key +" : "+value)
            except:
                print("Data is not printing in the text box")   
        self.thread.send_data(find_message)

    def test(self):
        self.ui.modelNoInput.setText(type_to_model[self.ui.typeInput.currentText()])

    def select_port(self):
        port_name = self.ui.comPortInput.currentText()[0:4]
        self.serial_port.port = port_name

    def receive_fb(self,fb):
        index = 0
        config_list = []
        for idx,char in enumerate(fb):
            if(char == "\r"):
                config_list_item = fb[index:idx]
                config_list.append(config_list_item)
                index = idx+1
        self.ui.serialNoInput.setText(config_list[3][4:])  
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("Feedback : "+fb)

    def configure(self):
        configure_info = "UNP\rCNG\rMDN:"+type_to_model[self.ui.typeInput.currentText()]+"\rSLN:"+self.ui.serialNoInput.text()+"\rSID:"+self.ui.slaveIdInput.text()+"\rBDR:"+str(self.ui.baudRateInput.currentIndex())+"\rPRB:"+str(self.ui.parityInput.currentIndex())+"\r\n"
        print(configure_info)
        self.thread.send_data(configure_info)
