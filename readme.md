## To compile a UI file to python file

```pyside6-uic [relative path to source]/filename.ui > [relative path to destination]/file_name.py```

## To compile a resource file to python file
```pyside6-rcc  [relative path to source]/filename.qrc -o [relative path to destination]/file_name.py```


### About Device-Config
Device-Config is a configuration software that configure device like Remote IO,Gateway.
### How it works?
To configure a device first,we need to setup a communication between the software and the device.
Then we follow two steps to configure the device.
First,the software sends a message (which we call find message) to the device to know the existing configuration of the device.Then the device sends a message contain it's configuration as a feedback to the software.
Second,When we get the feedback message then we custome the configuration how we want to configure the device and sends the configuration info to the device and if the device get the configuration info it send the software a successful message as a feedback.
### How the software access the port and comunicate with the device?
To comunicate with the device we need to access the port first.To accessing the port we use pySerial library.After accesing the port and establishing the communication between the device and the software we use write() function of pySerial to send the message to the device.And to receive the message from the device we use the read() function.
### How dose the software know there is a feedback?
Suppose, this software connect with port "COM5".Now it will use this port to send the message as well as receice the message.And also when the software use this port to send message it cann't use it to receive message untill close the port and reopen the port for receiving perpose.
To solve this porblem we use Qthread which is a thread of QT.We use this thread to always be ready for receiving any message or feedback.And we make an interrupt in this receiving mode using a flag when need to send a message.
### How to catch the feedback in mainwindow from the thread?
We create a signal in the thread and emit it.Wheneve the feedback arrive the signal emit the data and there is a slot in the mainwindow which will take the feedback.
