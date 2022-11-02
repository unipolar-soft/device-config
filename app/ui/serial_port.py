import sys, time
from PySide6.QtGui import *
from PySide6.QtCore import *
import serial.tools.list_ports as port_list
import serial


class SerialPort(QThread):
    def __init__(self):
        super(SerialPort, self).__init__()
        self.send_flag = False
        self.serial_port = serial.Serial()
        self.serial_port.port = "COM5"
        self.serial_port.baudrate=115200
        self.serial_port.bytesize=8
        self.serial_port.timeout=10
        self.serial_port.stopbits=serial.STOPBITS_ONE
        self.serial_port.open()
        self.message = None
        self.feedback = Signal(int)

    def run(self):
        while(True):
            print("thread is running")
            if(self.send_flag == True):
                self.data_sending()
                self.send_flag = False
            else:
                bytesToRead = self.serial_port.inWaiting()
                data = self.serial_port.readline(bytesToRead)
                if data == b'':
                    time.sleep(1)
                print(data.decode())  
                self.feedback.emit(data.decode()) 

    def data_sending(self):
        print("calling from sending")
        self.serial_port.write(('COM Port :'+self.message["COM_port"]+"\n").encode())

    def send_data(self,message):
        self.send_flag = True       
        self.message = message

    def feedback(self):
        print("feedback function is giving feedback")