from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiSubWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, \
    QMessageBox, QInputDialog

from ui.slave_main_window.ui_slave_main_window import Ui_SlaveMainWindow


class CustomBlock(QMdiSubWindow):
    """
    Customized QMdiSubWindow class.
    """

    title_double_clicked = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.title_double_clicked.emit()
        super().mouseDoubleClickEvent(event)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.closed.emit()


class SlaveMainWindow(QMainWindow, Ui_SlaveMainWindow):
    def __init__(self):
        """
        Slave main window constructor.
        """
        super().__init__()
        self.block_counter = 0
        self.limit_blocks = 5
        self.blocks = []
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the main window.
        """
        self.addModbusBlockBtn.clicked.connect(self.add_block)
        self.deleteBlocksBtn.clicked.connect(self.delete_all_blocks)
        self.add_block()

    def add_block(self):
        """
        Add a block to the main window.
        """
        if self.block_counter < self.limit_blocks:
            self.block_counter += 1
            sub_window = CustomBlock()
            text_edit = QTextEdit()
            sub_window.setWidget(text_edit)
            sub_window.setWindowTitle(f"New block")

            # Connect double-click signal to edit title
            sub_window.title_double_clicked.connect(lambda: self.edit_title(sub_window))

            sub_window.closed.connect(lambda: self.block_closed_event(sub_window))

            self.blocks.append(sub_window)
            self.blocksContainer.addSubWindow(sub_window)
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

    def edit_title(self, sub_window: QMdiSubWindow):
        """
        Handle title edit when double-clicked.

        :param sub_window: QMdiSubWindow to edit the title.
        """
        new_title, ok = QInputDialog.getText(self, "Edit Title", "Enter new title:", text=sub_window.windowTitle())

        if ok and new_title:
            sub_window.setWindowTitle(new_title)


