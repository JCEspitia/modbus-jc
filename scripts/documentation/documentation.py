import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QFile
from ui.documentation.ui_documentation import Ui_Documentation


class Documentation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Documentation()
        self.ui.setupUi(self)

        # Conectar señales y slots si es necesario

        self.load_html_from_file('docs/documentation.html')

    def load_html_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.ui.docViewer.setHtml(html_content)
        except FileNotFoundError:
            print(f'Error: El archivo {file_path} no se encontró.')
