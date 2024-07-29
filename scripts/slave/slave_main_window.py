from PyQt6.QtWidgets import QMainWindow, QMdiSubWindow, QMessageBox, QInputDialog

from scripts.settings.settings_dialog import SettingsDialog
from scripts.registers_widget.registers_widget_container import RegistersWidgetContainer
from scripts.slave.slave_settings import SlaveConfigDialog
from ui.slave_main_window.ui_slave_main_window import Ui_SlaveMainWindow


class SlaveMainWindow(QMainWindow, Ui_SlaveMainWindow):
    def __init__(self, window_manager=None):
        """
        Slave main window constructor.
        """
        super().__init__()
        self.block_counter = 0
        self.limit_blocks = 5
        self.blocks = []
        self.setupUi(self)
        self.initialize_ui()
        self.window_manager = window_manager

    def initialize_ui(self):
        """
        Initialize the main window.
        """
        self.actionHome.triggered.connect(self.open_home)
        self.actionAddBlock.triggered.connect(self.add_block)
        self.actionDeleteBlocks.triggered.connect(self.delete_all_blocks)
        self.actionSlaveSettings.triggered.connect(self.open_slave_config_dialog)
        self.actionSettings.triggered.connect(self.open_settings_dialog)
        self.add_block()

    def open_home(self):
        self.window_manager.show_home()
        self.close()

    def open_slave_config_dialog(self):
        """
        Show the SlaveConfigDialog.
        """
        SlaveConfigDialog(self).exec()

    def open_settings_dialog(self):
        """
        Show the ConfigurationDialog.
        """
        SettingsDialog(self).exec()

    def add_block(self):
        """
        Add a block to the main window.
        """
        if self.block_counter < self.limit_blocks:
            self.block_counter += 1
            sub_window = RegistersWidgetContainer()
            sub_window.setWindowTitle("New block")

            sub_window.title_double_clicked.connect(lambda: sub_window.open_slave_config_dialog())

            sub_window.closed.connect(lambda: self.block_closed_event(sub_window))

            self.blocks.append(sub_window)
            self.blocksContainer.addSubWindow(sub_window)
            sub_window.resize(300, 400)
            sub_window.show()
        else:
            QMessageBox.warning(self,
                                "Lots of blocks!",
                                f"The limit of simultaneous blocks has been exceeded (maximum {self.limit_blocks})"
                                )

    def delete_all_blocks(self):
        """
        Delete all blocks from the main window.
        """
        self.blocksContainer.closeAllSubWindows()
        self.blocks = []
        self.block_counter = 0

    def block_closed_event(self, sub_window: QMdiSubWindow):
        """
        Event handler for the closed QMdiSubWindow.

        :param sub_window: Closed QMdiSubWindow.
        """
        if sub_window in self.blocks:
            self.blocks.remove(sub_window)
            self.block_counter -= 1
