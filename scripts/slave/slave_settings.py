from PyQt6.QtWidgets import QDialog
from ui.slave_settings_dialog.ui_slave_settings_dialog import Ui_SlaveSettingsDialog


class SlaveConfigDialog(QDialog, Ui_SlaveSettingsDialog):
    def __init__(self, parent=None):
        """
            Description
        """
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the widget.
        """
        pass

