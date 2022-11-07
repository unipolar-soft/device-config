from PySide6.QtWidgets import QMainWindow
from .ui.ui_connect import Ui_Dialog



class Connect(QMainWindow):
    def __init__(self,parent=None):
        super(Connect, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)