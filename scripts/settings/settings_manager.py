from PyQt6.QtCore import QSettings


class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Inicializar QSettings
            cls._instance.settings = QSettings("ModbusJC", "ModbusJC")
        return cls._instance

    @staticmethod
    def get_instance():
        if SettingsManager._instance is None:
            SettingsManager()
        return SettingsManager._instance.settings
