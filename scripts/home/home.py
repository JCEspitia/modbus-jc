from PyQt6 import QtWidgets

from ui.home.ui_home import Ui_Home
from scripts.settings.settings_dialog import SettingsDialog


class Home(QtWidgets.QMainWindow, Ui_Home):
    def __init__(self, app, window_manager=None):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.window_manager = window_manager
        self.initialize_ui()

    def initialize_ui(self):
        self.modbusSlaveBtn.clicked.connect(self.open_slave_main_window)
        self.modbusMasterBtn.clicked.connect(self.open_master_main_window)
        self.configBtn.clicked.connect(self.open_configuration_dialog)
        self.docBtn.clicked.connect(self.open_documentation)
        self.exitBtn.clicked.connect(QtWidgets.QApplication.quit)

    def open_slave_main_window(self):
        self.window_manager.show_slave_main_window()

    def open_master_main_window(self):
        self.window_manager.show_master_main_window()

    def open_documentation(self):
        self.window_manager.show_documentation()

    def open_configuration_dialog(self):
        SettingsDialog(self).exec()
