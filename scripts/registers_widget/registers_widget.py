from math import ceil

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QStyledItemDelegate, QLineEdit

from ui.registers_widget.ui_registers_widget import Ui_RegistersWidget


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


class RegistersWidget(QWidget, Ui_RegistersWidget):
    def __init__(self):
        """
            Description
        """
        super().__init__()
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the widget.
        """
        pass

    def update_table(self, initial_register, quantity):
        rows = 10  # Default 10 rows
        cols = ceil(quantity / rows) * 2

        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        # Añadir encabezados de columna alternando entre "Register" y "Value"
        headers = []
        for i in range(cols):
            if i % 2 == 0:
                headers.append(f"Register")
            else:
                headers.append(f"Value")
        self.tableWidget.setHorizontalHeaderLabels(headers)

        block_count = 0
        for col in range(0, cols, 2):
            for row in range(rows):
                if block_count >= quantity:
                    self.disable_cell(row, col)
                else:
                    register_number = initial_register + block_count
                    self.tableWidget.setItem(row, col, QTableWidgetItem(f"Register {register_number}"))
                    self.tableWidget.setItem(row, col + 1, QTableWidgetItem("0"))
                    block_count += 1

        # Asignar el delegado numérico a las columnas de valores
        numeric_delegate = NumericDelegate()
        for col in range(1, cols, 2):
            self.tableWidget.setItemDelegateForColumn(col, numeric_delegate)

    def disable_cell(self, row, col):
        for i in range(2):
            item = QTableWidgetItem("")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
            self.tableWidget.setItem(row, col + i, item)
