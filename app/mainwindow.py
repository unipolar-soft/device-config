# This Python file uses the following encoding: utf-8
from cgi import test
import os
from pathlib import Path
from select import select
import sys
import logging
from logging.config import dictConfig
import PySide6

from PySide6.QtWidgets import QMainWindow,QListWidgetItem
from PySide6.QtCore import Qt
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

dictConfig(DIC_LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)
type_to_model = {
    "2 CH AI,4 Ch DI" : "01",
    "4 CH AI" : "02",
    "8 CH DO" : "03"
}
port_name = "COM5"
serial_port  = serial.Serial(port=port_name, baudrate=115200, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        # Validate slave Id filed 
        validator = QIntValidator(1,147, self)
        self.input = self.ui.slaveIdInput.setValidator(validator)
        self.ui.findDevice.clicked.connect(self.find_device)
        self.ui.typeInput.currentTextChanged.connect(self.test)
        # map the device type to model
        self.ui.modelNoInput.setText(type_to_model[self.ui.typeInput.currentText()])
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
        for key, value in config.items():
            self.ui.listWidget.addItem( key +" : "+value)
        serial_port.write(('COM Port :'+config["COM_port"]+"\n").encode())
        # while(True):
        #     try:
        #         bytesToRead = serial_port.inWaiting()
        #         data = serial_port.readline(bytesToRead)
        #         if data == b'':
        #             time.sleep(1)
        #             continue
        #         print(data.decode())
        #     except:
        #         break    
    def test(self):
        self.ui.modelNoInput.setText(type_to_model[self.ui.typeInput.currentText()])
    def select_port(self):
        port_name = self.ui.comPortInput.currentText()[0:4]
        serial.Serial(port=port_name, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
