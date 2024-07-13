from PyQt6 import QtWidgets
from scripts.home.home import Home
from scripts.slave.slave_main_window import SlaveMainWindow
from scripts.master.master_main_window import MasterMainWindow
from scripts.documentation.documentation import Documentation


class WindowManager:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.home = Home(self)
        self.slave_main_window = SlaveMainWindow()
        self.master_main_window = MasterMainWindow()
        self.documentation = Documentation()

    def show_home(self):
        self.home.show()

    def show_slave_main_window(self):
        self.slave_main_window.show()

    def show_master_main_window(self):
        self.master_main_window.show()

    def show_documentation(self):
        self.documentation.show()

    def run(self):
        self.show_home()
        self.app.exec()
