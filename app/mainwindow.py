# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import logging
from logging.config import dictConfig

from PySide6.QtWidgets import QMainWindow
from .ui.ui_mainwindow import Ui_MainWindow
from .projutil.log_conf import DIC_LOGGING_CONFIG
from .projutil.conf import LOGGER_NAME

dictConfig(DIC_LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)