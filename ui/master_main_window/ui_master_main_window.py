# Form implementation generated from reading ui file 'ui/master_main_window/master_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MasterMainWindow(object):
    def setupUi(self, MasterMainWindow):
        MasterMainWindow.setObjectName("MasterMainWindow")
        MasterMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MasterMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MasterMainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(parent=MasterMainWindow)
        self.toolBar.setObjectName("toolBar")
        MasterMainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionHome = QtGui.QAction(parent=MasterMainWindow)
        icon = QtGui.QIcon.fromTheme("go-home")
        self.actionHome.setIcon(icon)
        self.actionHome.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionHome.setObjectName("actionHome")
        self.toolBar.addAction(self.actionHome)

        self.retranslateUi(MasterMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MasterMainWindow)

    def retranslateUi(self, MasterMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MasterMainWindow.setWindowTitle(_translate("MasterMainWindow", "Modbus JC - Master"))
        self.label.setText(_translate("MasterMainWindow", "COMIC SOON..."))
        self.toolBar.setWindowTitle(_translate("MasterMainWindow", "toolBar"))
        self.actionHome.setText(_translate("MasterMainWindow", "Home"))
