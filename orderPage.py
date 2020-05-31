# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class OrderPageUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 351, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Subjectlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Subjectlabel.setObjectName("Subjectlabel")
        self.gridLayout.addWidget(self.Subjectlabel, 0, 0, 1, 1)
        self.ShowSubjectlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ShowSubjectlabel.setText("")
        self.ShowSubjectlabel.setObjectName("ShowSubjectlabel")
        self.gridLayout.addWidget(self.ShowSubjectlabel, 0, 1, 1, 1)
        self.Reauiredlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Reauiredlabel.setObjectName("Reauiredlabel")
        self.gridLayout.addWidget(self.Reauiredlabel, 1, 0, 1, 1)
        self.Pricelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Pricelabel.setObjectName("Pricelabel")
        self.gridLayout.addWidget(self.Pricelabel, 2, 0, 1, 1)
        self.ShowRequiredlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ShowRequiredlabel.setText("")
        self.ShowRequiredlabel.setObjectName("ShowRequiredlabel")
        self.gridLayout.addWidget(self.ShowRequiredlabel, 1, 1, 1, 1)
        self.ShowPricelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ShowPricelabel.setText("")
        self.ShowPricelabel.setObjectName("ShowPricelabel")
        self.gridLayout.addWidget(self.ShowPricelabel, 2, 1, 1, 1)
        self.RespondpushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RespondpushButton.setObjectName("RespondpushButton")
        self.gridLayout.addWidget(self.RespondpushButton, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Order"))
        self.Subjectlabel.setText(_translate("Dialog", "Subject"))
        self.Reauiredlabel.setText(_translate("Dialog", "Who is required:"))
        self.Pricelabel.setText(_translate("Dialog", "Price"))
        self.RespondpushButton.setText(_translate("Dialog", "Respond"))

class orderPageController(QtWidgets.QDialog, OrderPageUI):
    def __init__(self, parent = None):
        super(orderPageController, self).__init__(parent)
        self.setupUi(self)
        self.RespondpushButton.clicked.connect(self.RespondpushButton_click)

    @QtCore.pyqtSlot()
    def RespondpushButton_click(self):
        print("RespondpushButton_click")
