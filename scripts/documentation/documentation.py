import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QFile
from ui.documentation.ui_documentation import Ui_Documentation


class Documentation(QMainWindow, Ui_Documentation):
    def __init__(self, window_manager=None):
        super().__init__()
        self.window_manager = window_manager
        self.setupUi(self)
        self.initialize_ui()

        # Conectar señales y slots si es necesario

        self.load_html_from_file('docs/documentation.html')

    def initialize_ui(self):
        """
        Initialize the main window.
        """
        self.actionHome.triggered.connect(self.open_home)

    def open_home(self):
        self.window_manager.show_home()
        self.close()

    def load_html_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.docViewer.setHtml(html_content)
        except FileNotFoundError:
            print(f'Error: El archivo {file_path} no se encontró.')
