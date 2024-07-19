import os
import sys

from PyQt6.QtCore import QTranslator
from PyQt6.QtWidgets import QDialog, QMessageBox, QApplication

from scripts.settings.settings_manager import SettingsManager
from ui.settings.ui_settings_dialog import Ui_SettingsDialog
from utils.custom_message_box.restart_message_box import RestartMessageBox


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, parent=None):
        """
            Description
        """
        super().__init__(parent)
        self.setupUi(self)
        self.settings = SettingsManager().get_instance()
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the widget.
        """
        self.initialize_language_cmb()

    def initialize_language_cmb(self):
        self.languageCmb.addItem("English", "en_US")
        self.languageCmb.addItem("Español", "es_ES")

        try:
            locale = self.settings.value('locale')
            default_index = self.languageCmb.findData(locale)  # Encuentra el índice del dato "en_US"

            if default_index != -1:
                self.languageCmb.setCurrentIndex(default_index)
        except Exception as e:
            print(e)

        self.languageCmb.currentIndexChanged.connect(self.on_language_change)

    def on_language_change(self, index):
        locale = self.languageCmb.itemData(index)
        self.settings.setValue("locale", locale)
        RestartMessageBox().show()
