# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 19, 341, 211))
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

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.passwordlabel.setText(_translate("Dialog", "Password"))
        self.userNamelabel.setText(_translate("Dialog", "User name"))
        self.createAccountPushButton.setText(_translate("Dialog", "create new account"))

class loginWindowController(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(loginWindowController, self).__init__(parent)
        self.setupUi(self)
        #self.SetPushButton.clicked.connect(self.setButton_click)
        #self.ConnectPushButton.clicked.connect(self.connectButton_click)
        #self.pushButtonConnectTest.clicked.connect(self.testConnectButton_click)
        #self.pushButtonSendTest.clicked.connect(self.testSendButton_click)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = loginWindowController()# = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    w.show()#MainWindow.show()
    sys.exit(app.exec_())
