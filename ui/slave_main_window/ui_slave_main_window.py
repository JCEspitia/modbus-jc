# Form implementation generated from reading ui file 'ui/slave_main_window/slave_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SlaveMainWindow(object):
    def setupUi(self, SlaveMainWindow):
        SlaveMainWindow.setObjectName("SlaveMainWindow")
        SlaveMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=SlaveMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blocksContainer = QtWidgets.QMdiArea(parent=self.centralwidget)
        self.blocksContainer.setObjectName("blocksContainer")
        self.verticalLayout.addWidget(self.blocksContainer)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        SlaveMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SlaveMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuFile.setObjectName("menuFile")
        self.menuConnection = QtWidgets.QMenu(parent=self.menubar)
        self.menuConnection.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuConnection.setObjectName("menuConnection")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetup = QtWidgets.QMenu(parent=self.menubar)
        self.menuSetup.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuSetup.setObjectName("menuSetup")
        self.menuFunctions = QtWidgets.QMenu(parent=self.menubar)
        self.menuFunctions.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuDisplay = QtWidgets.QMenu(parent=self.menubar)
        self.menuDisplay.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuDisplay.setObjectName("menuDisplay")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(parent=self.menubar)
        self.menuWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuWindow.setObjectName("menuWindow")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuHelp.setObjectName("menuHelp")
        SlaveMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SlaveMainWindow)
        self.statusbar.setObjectName("statusbar")
        SlaveMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=SlaveMainWindow)
        self.toolBar.setObjectName("toolBar")
        SlaveMainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionHome = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("go-home")
        self.actionHome.setIcon(icon)
        self.actionHome.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionHome.setObjectName("actionHome")
        self.actionAddBlock = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.actionAddBlock.setIcon(icon)
        self.actionAddBlock.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionAddBlock.setObjectName("actionAddBlock")
        self.actionDeleteBlocks = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.actionDeleteBlocks.setIcon(icon)
        self.actionDeleteBlocks.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionDeleteBlocks.setObjectName("actionDeleteBlocks")
        self.actionSlaveSettings = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("system-run")
        self.actionSlaveSettings.setIcon(icon)
        self.actionSlaveSettings.setObjectName("actionSlaveSettings")
        self.actionSettings = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("document-properties")
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSave = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtGui.QAction(parent=SlaveMainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuSetup.addAction(self.actionSlaveSettings)
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
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionAddBlock)
        self.toolBar.addAction(self.actionDeleteBlocks)

        self.retranslateUi(SlaveMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SlaveMainWindow)

    def retranslateUi(self, SlaveMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SlaveMainWindow.setWindowTitle(_translate("SlaveMainWindow", "Modbus JC - Slave"))
        self.menuFile.setTitle(_translate("SlaveMainWindow", "File"))
        self.menuConnection.setTitle(_translate("SlaveMainWindow", "Connection"))
        self.menuEdit.setTitle(_translate("SlaveMainWindow", "Edit"))
        self.menuSetup.setTitle(_translate("SlaveMainWindow", "Setup"))
        self.menuFunctions.setTitle(_translate("SlaveMainWindow", "Functions"))
        self.menuDisplay.setTitle(_translate("SlaveMainWindow", "Display"))
        self.menuView.setTitle(_translate("SlaveMainWindow", "View"))
        self.menuWindow.setTitle(_translate("SlaveMainWindow", "Window"))
        self.menuTools.setTitle(_translate("SlaveMainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("SlaveMainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("SlaveMainWindow", "toolBar"))
        self.actionHome.setText(_translate("SlaveMainWindow", "Go to home"))
        self.actionAddBlock.setText(_translate("SlaveMainWindow", "Add new block"))
        self.actionDeleteBlocks.setText(_translate("SlaveMainWindow", "Delete all blocks"))
        self.actionSlaveSettings.setText(_translate("SlaveMainWindow", "Slave Settings..."))
        self.actionSlaveSettings.setToolTip(_translate("SlaveMainWindow", "Slave settings"))
        self.actionSettings.setText(_translate("SlaveMainWindow", "Settings"))
        self.actionSave.setText(_translate("SlaveMainWindow", "Save"))
        self.actionSave_as.setText(_translate("SlaveMainWindow", "Save As..."))
        self.actionNew.setText(_translate("SlaveMainWindow", "New..."))
