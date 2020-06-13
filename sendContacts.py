# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendContacts.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import database_func as db

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 202)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 311, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your contacts:"))
        self.pushButton.setText(_translate("Dialog", "Ok"))


class sendContactsController(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, id: int,parent = None):
        self.orderId = id
        super(sendContactsController, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)

    @QtCore.pyqtSlot()
    def pushButton_clicked(self):
        print("pushButton_clicked")
        contact = self.lineEdit.text()
        dbtofindorder = db.database("orderDB")
        dbtofindorder.readFromFile("orderdb.txt")
        element = dbtofindorder.returnWithId(self.orderId)
        #(self, fileName, id, _subject: str, _author: str, _whoReq: str, _price: str, _status: str)
        orderDB = db.database("orderDB")
        orderDB.modify("orderdb.txt", self.orderId, element.subject, element.author, element.whoRequired, element.price, "respond " + contact)