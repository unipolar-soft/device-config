import string
import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
import serial.tools.list_ports as port_list
import serial


class SerialPort(QThread):

    feedback = Signal(str)

    def __init__(self):
        super(SerialPort, self).__init__()
        self.send_flag = False
        self.serial = serial.Serial()
        self.serial.port = "COM5"
        self.serial.baudrate=115200
        self.serial.bytesize=8
        self.serial.timeout=10
        self.serial.stopbits=serial.STOPBITS_ONE
        self.serial.open()
        self.message = None

    def run(self):
        print("thread is running")
        while(True):
            if(self.send_flag == True):
                self.data_sending()
                self.send_flag = False
            else:
                bytesToRead = self.serial.inWaiting()
                data = self.serial.readline(bytesToRead)
                if data == b'':
                    time.sleep(1)
                if data != b'' and data != ' ':
                    self.feedback.emit(data.decode())   

    def data_sending(self):
        self.serial.write((self.message).encode())

    def send_data(self,message):
        self.send_flag = True       
        self.message = message