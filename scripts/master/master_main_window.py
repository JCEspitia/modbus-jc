from PyQt6 import QtWidgets
from ui.master_main_window.ui_master_main_window import Ui_MasterMainWindow


class MasterMainWindow(QtWidgets.QMainWindow, Ui_MasterMainWindow):
    def __init__(self, window_manager=None):
        super().__init__()
        self.window_manager = window_manager
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the main window.
        """
        self.actionHome.triggered.connect(self.open_home)

    def open_home(self):
        self.window_manager.show_home()
        self.close()
