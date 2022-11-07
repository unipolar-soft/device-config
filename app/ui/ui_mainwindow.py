# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(386, 608)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionRemote_IO = QAction(MainWindow)
        self.actionRemote_IO.setObjectName(u"actionRemote_IO")
        self.actionGateway = QAction(MainWindow)
        self.actionGateway.setObjectName(u"actionGateway")
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 331, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 271, 252))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.device = QLabel(self.layoutWidget)
        self.device.setObjectName(u"device")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.device)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.type = QLabel(self.layoutWidget)
        self.type.setObjectName(u"type")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.type)

        self.typeInput = QComboBox(self.layoutWidget)
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.setObjectName(u"typeInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.typeInput)

        self.modelNo = QLabel(self.layoutWidget)
        self.modelNo.setObjectName(u"modelNo")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.modelNo)

        self.modelNoInput = QLineEdit(self.layoutWidget)
        self.modelNoInput.setObjectName(u"modelNoInput")
        self.modelNoInput.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.modelNoInput)

        self.serialNo = QLabel(self.layoutWidget)
        self.serialNo.setObjectName(u"serialNo")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.serialNo)

        self.serialNoInput = QLineEdit(self.layoutWidget)
        self.serialNoInput.setObjectName(u"serialNoInput")
        self.serialNoInput.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.serialNoInput)

        self.slaveId = QLabel(self.layoutWidget)
        self.slaveId.setObjectName(u"slaveId")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.slaveId)

        self.slaveIdInput = QLineEdit(self.layoutWidget)
        self.slaveIdInput.setObjectName(u"slaveIdInput")
        self.slaveIdInput.setMaxLength(247)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.slaveIdInput)

        self.baudRate = QLabel(self.layoutWidget)
        self.baudRate.setObjectName(u"baudRate")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.baudRate)

        self.baudRateInput = QComboBox(self.layoutWidget)
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.addItem("")
        self.baudRateInput.setObjectName(u"baudRateInput")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.baudRateInput)

        self.parity = QLabel(self.layoutWidget)
        self.parity.setObjectName(u"parity")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.parity)

        self.parityInput = QComboBox(self.layoutWidget)
        self.parityInput.addItem("")
        self.parityInput.addItem("")
        self.parityInput.addItem("")
        self.parityInput.setObjectName(u"parityInput")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.parityInput)

        self.findDevice = QPushButton(self.layoutWidget)
        self.findDevice.setObjectName(u"findDevice")
        self.findDevice.setStyleSheet(u"")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.findDevice)

        self.configure = QPushButton(self.layoutWidget)
        self.configure.setObjectName(u"configure")
        self.configure.setStyleSheet(u"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.configure)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comPortInput = QComboBox(self.layoutWidget)
        self.comPortInput.setObjectName(u"comPortInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comPortInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 270, 271, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 386, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuDevice = QMenu(self.menuMenu)
        self.menuDevice.setObjectName(u"menuDevice")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.menuDevice.menuAction())
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionConnect)
        self.menuMenu.addAction(self.actionDisconnect)
        self.menuDevice.addAction(self.actionRemote_IO)
        self.menuDevice.addAction(self.actionGateway)

        self.retranslateUi(MainWindow)

        self.baudRateInput.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRemote_IO.setText(QCoreApplication.translate("MainWindow", u"Remote IO", None))
        self.actionGateway.setText(QCoreApplication.translate("MainWindow", u"Gateway", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.device.setText(QCoreApplication.translate("MainWindow", u"Device :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Remote IO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gateway", None))

        self.type.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.typeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"2 CH AI,4 Ch DI", None))
        self.typeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"4 CH AI", None))
        self.typeInput.setItemText(2, QCoreApplication.translate("MainWindow", u"8 CH DO", None))

        self.modelNo.setText(QCoreApplication.translate("MainWindow", u"Model No :", None))
        self.modelNoInput.setText("")
        self.serialNo.setText(QCoreApplication.translate("MainWindow", u"Serial No :", None))
        self.slaveId.setText(QCoreApplication.translate("MainWindow", u"Slave ID :", None))
        self.slaveIdInput.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.slaveIdInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input number between 1 to 247", None))
        self.baudRate.setText(QCoreApplication.translate("MainWindow", u"Baud Rate :", None))
        self.baudRateInput.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.baudRateInput.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baudRateInput.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.baudRateInput.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.baudRateInput.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.baudRateInput.setItemText(5, QCoreApplication.translate("MainWindow", u"115200", None))
        self.baudRateInput.setItemText(6, QCoreApplication.translate("MainWindow", u"230400", None))

        self.parity.setText(QCoreApplication.translate("MainWindow", u"Parity :", None))
        self.parityInput.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.parityInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.parityInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Even", None))

        self.findDevice.setText(QCoreApplication.translate("MainWindow", u"Find Device", None))
        self.configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"COM Port :", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuDevice.setTitle(QCoreApplication.translate("MainWindow", u"Device", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

