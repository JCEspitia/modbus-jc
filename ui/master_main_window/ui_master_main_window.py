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
        MasterMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MasterMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuConnection = QtWidgets.QMenu(parent=self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetup = QtWidgets.QMenu(parent=self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuFunctions = QtWidgets.QMenu(parent=self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuDisplay = QtWidgets.QMenu(parent=self.menubar)
        self.menuDisplay.setObjectName("menuDisplay")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(parent=self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MasterMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MasterMainWindow)
        self.statusbar.setObjectName("statusbar")
        MasterMainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MasterMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MasterMainWindow)

    def retranslateUi(self, MasterMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MasterMainWindow.setWindowTitle(_translate("MasterMainWindow", "Modbus JC - Master"))
        self.menuFile.setTitle(_translate("MasterMainWindow", "File"))
        self.menuConnection.setTitle(_translate("MasterMainWindow", "Connection"))
        self.menuEdit.setTitle(_translate("MasterMainWindow", "Edit"))
        self.menuSetup.setTitle(_translate("MasterMainWindow", "Setup"))
        self.menuFunctions.setTitle(_translate("MasterMainWindow", "Functions"))
        self.menuDisplay.setTitle(_translate("MasterMainWindow", "Display"))
        self.menuView.setTitle(_translate("MasterMainWindow", "View"))
        self.menuWindow.setTitle(_translate("MasterMainWindow", "Window"))
        self.menuTools.setTitle(_translate("MasterMainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MasterMainWindow", "Help"))