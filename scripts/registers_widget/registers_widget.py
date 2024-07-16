from PyQt6.QtWidgets import QWidget

from ui.registers_widget.ui_registers_widget import Ui_RegistersWidget


class RegistersWidget(QWidget, Ui_RegistersWidget):
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
