from PyQt6.QtWidgets import QDialog
from ui.slave_configuration_dialog.ui_slave_configuration_dialog import Ui_SlaveConfigDialog


class SlaveConfigDialog(QDialog, Ui_SlaveConfigDialog):
    def __init__(self):
        """
            Description
        """
        super().__init__()
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the widget.
        """
        pass

