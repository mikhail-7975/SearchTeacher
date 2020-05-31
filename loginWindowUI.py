# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class logInWindowUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 19, 341, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.passwordlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passwordlabel.setObjectName("passwordlabel")
        self.gridLayout.addWidget(self.passwordlabel, 1, 0, 1, 1)
        self.userNamelineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userNamelineEdit.setObjectName("userNamelineEdit")
        self.gridLayout.addWidget(self.userNamelineEdit, 0, 1, 1, 1)
        self.passwordlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.gridLayout.addWidget(self.passwordlineEdit, 1, 1, 1, 1)
        self.userNamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.userNamelabel.setObjectName("userNamelabel")
        self.gridLayout.addWidget(self.userNamelabel, 0, 0, 1, 1)
        self.createAccountPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.createAccountPushButton.setObjectName("createAccountPushButton")
        self.gridLayout.addWidget(self.createAccountPushButton, 2, 0, 1, 1)
        self.LogInPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LogInPushButton.setObjectName("LogInPushButton")
        self.gridLayout.addWidget(self.LogInPushButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.passwordlabel.setText(_translate("Dialog", "Password"))
        self.userNamelabel.setText(_translate("Dialog", "User name"))
        self.createAccountPushButton.setText(_translate("Dialog", "create new account"))
        self.LogInPushButton.setText(_translate("Dialog", "Log in"))

class loginWindowController(QtWidgets.QDialog, logInWindowUI):
    login = "hello world"
    password = "123456"
    allowLogin = 0
    def __init__(self, parent = None):
        super(loginWindowController, self).__init__(parent)
        self.setupUi(self)
        self.createAccountPushButton.clicked.connect(self.createAccountPushButton_click)
        self.LogInPushButton.clicked.connect(self.LogInPushButton_click)

    @QtCore.pyqtSlot()
    def createAccountPushButton_click(self):
        print("createAccountPushButton clicked")

    @QtCore.pyqtSlot()
    def LogInPushButton_click(self):
        print("LogInPushButton_click")
        print(self.userNamelineEdit.text(), " == ", self.login, "?")
        if(self.userNamelineEdit.text() == self.login):
            print("yes")
            self.allowLogin = 0
        



