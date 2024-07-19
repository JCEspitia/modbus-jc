# restart_message_box.py
from PyQt6.QtWidgets import QMessageBox, QApplication
import sys
import os


class RestartMessageBox:
    @staticmethod
    def show(title='Restart aplication', text="To apply the changes the software must be restarted",
             informative_text=None, text_restart_btn='Restart now', text_ok_btn='Restart later'):
        # Crear un QMessageBox
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        if informative_text:
            msg_box.setInformativeText(informative_text)

        # Agregar botones personalizados
        restart_button = msg_box.addButton(text_restart_btn, QMessageBox.ButtonRole.AcceptRole)
        ok_button = msg_box.addButton(text_ok_btn, QMessageBox.ButtonRole.RejectRole)

        # Establecer el botón predeterminado (Opcional)
        msg_box.setDefaultButton(ok_button)

        msg_box.exec()

        # Manejar la respuesta del usuario
        if msg_box.clickedButton() == restart_button:
            RestartMessageBox.restart_application()

    @staticmethod
    def restart_application():
        # Reiniciar la aplicación
        QApplication.instance().quit()  # Termina la aplicación actual

        # Reiniciar la aplicación
        python = sys.executable
        os.execl(python, python, *sys.argv)
