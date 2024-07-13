from PyQt6 import QtWidgets
from ui.master_main_window.ui_master_main_window import Ui_MasterMainWindow


class MasterMainWindow(QtWidgets.QMainWindow, Ui_MasterMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

