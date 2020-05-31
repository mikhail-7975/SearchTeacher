# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newOrder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newOrder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NewOrderUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 29, 341, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Pricelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Pricelabel.setObjectName("Pricelabel")
        self.gridLayout.addWidget(self.Pricelabel, 2, 0, 1, 1)
        self.SetRolecomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.SetRolecomboBox.setObjectName("SetRolecomboBox")
        self.gridLayout.addWidget(self.SetRolecomboBox, 1, 1, 1, 1)
        self.Subjectlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Subjectlabel.setObjectName("Subjectlabel")
        self.gridLayout.addWidget(self.Subjectlabel, 0, 0, 1, 1)
        self.SetSubjectcomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.SetSubjectcomboBox.setObjectName("SetSubjectcomboBox")
        self.gridLayout.addWidget(self.SetSubjectcomboBox, 0, 1, 1, 1)
        self.Rolelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Rolelabel.setObjectName("Rolelabel")
        self.gridLayout.addWidget(self.Rolelabel, 1, 0, 1, 1)
        self.SetPricelineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SetPricelineEdit.setObjectName("SetPricelineEdit")
        self.gridLayout.addWidget(self.SetPricelineEdit, 2, 1, 1, 1)
        self.CreateOrderPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CreateOrderPushButton.setObjectName("CreateOrderPushButton")
        self.gridLayout.addWidget(self.CreateOrderPushButton, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New order"))
        self.Pricelabel.setText(_translate("Dialog", "Price for hour"))
        self.Subjectlabel.setText(_translate("Dialog", "TextLabel"))
        self.Rolelabel.setText(_translate("Dialog", "I want to found "))
        self.CreateOrderPushButton.setText(_translate("Dialog", "Create"))


class newOrderPageController(QtWidgets.QDialog, NewOrderUi):
    def __init__(self, parent = None):
        super(newOrderPageController, self).__init__(parent)
        self.setupUi(self)
        self.CreateOrderPushButton.clicked.connect(self.CreateOrderPushButton_clicked)

        @QtCore.pyqtSlot()
        def CreateOrderPushButton_clicked(self):
            print("CreateOrderPushButton_clicked")