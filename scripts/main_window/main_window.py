from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings

from scripts.settings.settings_manager import SettingsManager
from ui.main_window.ui_main_window import Ui_MainWindow

from scripts.home.home import Home
from scripts.slave.slave_main_window import SlaveMainWindow
from scripts.master.master_main_window import MasterMainWindow
from scripts.documentation.documentation import Documentation


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.settings = SettingsManager().get_instance()
        self.home = Home(app, self)
        self.slave_main_window = SlaveMainWindow(self)
        self.master_main_window = MasterMainWindow(self)
        self.documentation = Documentation(self)

        self.initialize_ui()

    def initialize_ui(self):
        self.set_user_settings()
        self.pageContainer.addWidget(self.home)
        self.pageContainer.addWidget(self.slave_main_window)
        self.pageContainer.addWidget(self.master_main_window)
        self.pageContainer.addWidget(self.documentation)
        self.show_home()

    def set_user_settings(self):
        try:
            self.resize(self.settings.value('window_size'))
            self.move(self.settings.value('window_position'))
        except Exception as e:
            print(e)

    def show_home(self):
        self.pageContainer.setCurrentWidget(self.home)

    def show_slave_main_window(self):
        self.pageContainer.setCurrentWidget(self.slave_main_window)

    def show_master_main_window(self):
        self.pageContainer.setCurrentWidget(self.master_main_window)

    def show_documentation(self):
        self.pageContainer.setCurrentWidget(self.documentation)

    def closeEvent(self, event):
        self.settings.setValue("window_size", self.size())
        self.settings.setValue("window_position", self.pos())
