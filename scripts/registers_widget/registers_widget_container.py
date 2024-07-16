from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QMdiSubWindow, QWidget, QInputDialog

from scripts.registers_widget.registers_widget import RegistersWidget


class RegistersWidgetContainer(QMdiSubWindow):
    """
    Customized QMdiSubWindow class.
    """

    title_double_clicked = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.content_widget = RegistersWidget()
        self.setWidget(self.content_widget)
        self.setAcceptDrops(True)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.title_double_clicked.emit()
            # Evitar que se maximice
            event.ignore()
        else:
            super().mouseDoubleClickEvent(event)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.closed.emit()

    def edit_title(self):
        """
        Handle title edit when double-clicked.
        """
        new_title, ok = QInputDialog.getText(self,
                                             "Edit Title",
                                             "Enter new title of block:",
                                             text=self.windowTitle())

        if ok and new_title:
            self.setWindowTitle(new_title)
