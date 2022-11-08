import time
from PySide6.QtGui import *
from PySide6.QtCore import *
import serial

# This is a thread and will start when the program start
class SerialPort(QThread):

    feedback = Signal(str)

    def __init__(self):
        super(SerialPort, self).__init__()
        self.send_flag = False           # Flag for interruption.
        self.serial = serial.Serial()    # Initialize the serail port for accessing port.
        self.serial.port = None      # Set the initial parameter of serial port.
        self.serial.baudrate=115200
        self.serial.bytesize=8
        self.serial.timeout=10
        self.serial.stopbits=serial.STOPBITS_ONE
        # self.serial.open()               # open the serial port.
        self.message = None

# This run function is a default function of this thread.This run function will be automatically called when this thread start.
# This function always listens port for the feedback.I also send data to the connected device depending on send flag. 
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
# This function is used for sending message to the connected device.
    def data_sending(self):
        self.serial.write((self.message).encode())
# This function is used for taking message which is given by the user.
# Also used for setting send flag.
    def send_data(self,message):
        self.send_flag = True       
        self.message = message

    def port_setup(self,port):
        self.serial.port = port
        self.serial.open() 