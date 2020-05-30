# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cancelOrder.ui'
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PurpoueLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PurpoueLabel.setObjectName("PurpoueLabel")
        self.gridLayout.addWidget(self.PurpoueLabel, 0, 0, 1, 1)
        self.PurpouselineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PurpouselineEdit.setObjectName("PurpouselineEdit")
        self.gridLayout.addWidget(self.PurpouselineEdit, 0, 1, 1, 1)
        self.Marklabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Marklabel.setObjectName("Marklabel")
        self.gridLayout.addWidget(self.Marklabel, 1, 0, 1, 1)
        self.RatingspinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.RatingspinBox.setObjectName("RatingspinBox")
        self.gridLayout.addWidget(self.RatingspinBox, 1, 1, 1, 1)
        self.cancelOrderPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancelOrderPushButton.setObjectName("cancelOrderPushButton")
        self.gridLayout.addWidget(self.cancelOrderPushButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cancel an order"))
        self.PurpoueLabel.setText(_translate("Dialog", "Purpose"))
        self.Marklabel.setText(_translate("Dialog", "Rating"))
        self.cancelOrderPushButton.setText(_translate("Dialog", "Cancel an order"))
