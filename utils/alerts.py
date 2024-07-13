from PyQt6.QtWidgets import QMessageBox, QWidget


def show_simple_alert(parent: QWidget, title: str = "Alert!", message: str = ""):
    """
        Run a simple alert with a custom message

        :param parent: Parent widget.
        :param title: Alert title.
        :param message: Alert message.
    """

    dlg = QMessageBox(parent)
    dlg.setWindowTitle(title)
    dlg.setText(message)
    dlg.exec()
