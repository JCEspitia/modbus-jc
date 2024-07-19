from PyQt6 import QtWidgets
from PyQt6.QtCore import QLocale, QTranslator

from scripts.main_window.main_window import MainWindow
from scripts.settings.settings_manager import SettingsManager

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    settings = SettingsManager().get_instance()

    try:
        locale = settings.value('locale')
        translator = QTranslator()
        if translator.load(f"translations/{locale}.qm"):
            app.installTranslator(translator)
        else:
            print(f"Error: No se pudo cargar el archivo de traducción {locale}.qm")
    except Exception as e:
        print(e)

    MainWindow(app).show()
    app.exec()
