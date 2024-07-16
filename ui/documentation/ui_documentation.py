# Form implementation generated from reading ui file 'ui/documentation/documentation.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Documentation(object):
    def setupUi(self, Documentation):
        Documentation.setObjectName("Documentation")
        Documentation.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Documentation)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.docViewer = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.docViewer.setReadOnly(True)
        self.docViewer.setObjectName("docViewer")
        self.verticalLayout.addWidget(self.docViewer)
        Documentation.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(parent=Documentation)
        self.toolBar.setObjectName("toolBar")
        Documentation.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionHome = QtGui.QAction(parent=Documentation)
        icon = QtGui.QIcon.fromTheme("go-home")
        self.actionHome.setIcon(icon)
        self.actionHome.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionHome.setObjectName("actionHome")
        self.toolBar.addAction(self.actionHome)

        self.retranslateUi(Documentation)
        QtCore.QMetaObject.connectSlotsByName(Documentation)

    def retranslateUi(self, Documentation):
        _translate = QtCore.QCoreApplication.translate
        Documentation.setWindowTitle(_translate("Documentation", "Modbus JC - Documentation"))
        self.toolBar.setWindowTitle(_translate("Documentation", "toolBar"))
        self.actionHome.setText(_translate("Documentation", "Home"))
