# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newOrder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import database_func as db

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 29, 341, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Subjectlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Subjectlabel.setObjectName("Subjectlabel")
        self.gridLayout.addWidget(self.Subjectlabel, 1, 0, 1, 1)
        self.pricelineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pricelineEdit.setObjectName("pricelineEdit")
        self.gridLayout.addWidget(self.pricelineEdit, 3, 1, 1, 1)
        self.CreateOrderPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CreateOrderPushButton.setObjectName("CreateOrderPushButton")
        self.gridLayout.addWidget(self.CreateOrderPushButton, 4, 1, 1, 1)
        self.Rolelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Rolelabel.setObjectName("Rolelabel")
        self.gridLayout.addWidget(self.Rolelabel, 2, 0, 1, 1)
        self.SubjectLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SubjectLineEdit.setObjectName("SubjectLineEdit")
        self.gridLayout.addWidget(self.SubjectLineEdit, 1, 1, 1, 1)
        self.wantFindLneEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.wantFindLneEdit.setObjectName("wantFindLneEdit")
        self.gridLayout.addWidget(self.wantFindLneEdit, 2, 1, 1, 1)
        self.Pricelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Pricelabel.setObjectName("Pricelabel")
        self.gridLayout.addWidget(self.Pricelabel, 3, 0, 1, 1)
        self.yourNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yourNameLabel.setObjectName("yourNameLabel")
        self.gridLayout.addWidget(self.yourNameLabel, 0, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New order"))
        self.Subjectlabel.setText(_translate("Dialog", "Subject"))
        self.CreateOrderPushButton.setText(_translate("Dialog", "Create"))
        self.Rolelabel.setText(_translate("Dialog", "I want to found "))
        self.Pricelabel.setText(_translate("Dialog", "Price for hour"))
        self.yourNameLabel.setText(_translate("Dialog", "Your name"))



class newOrderPageController(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(newOrderPageController, self).__init__(parent)
        self.setupUi(self)
        print("CreateOrderPushButton.clicked.connect(self.CreateOrderPushButton_clicked)")
        self.CreateOrderPushButton.clicked.connect(self.CreateOrderPushButton_clicked)
        #self.CreateOrderPushButton.clicked.connect(self.close)

    @QtCore.pyqtSlot()
    def CreateOrderPushButton_clicked(self):
        print("CreateOrderPushButton_clicked")
        orderDataBase = db.database("orderDB")
        orderDataBase.readFromFile("orderdb.txt")
        orderDataBase.insert("OOD", "Stavro Evg.", "bestsenno", "created")
        orderDataBase.writeInFile("orderdb.txt")
