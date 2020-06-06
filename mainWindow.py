# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from newOrder import *

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 781, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainWindowTabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.mainWindowTabWidget.setObjectName("mainWindowTabWidget")
        self.UserPageTab = QtWidgets.QWidget()
        self.UserPageTab.setObjectName("UserPageTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.UserPageTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 771, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.userNameGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.userNameGridLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameGridLayout.setObjectName("userNameGridLayout")
        self.UserNamelabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.UserNamelabel.setObjectName("UserNamelabel")
        self.userNameGridLayout.addWidget(self.UserNamelabel, 0, 0, 1, 1)
        self.ShowUserNamelabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ShowUserNamelabel.setText("")
        self.ShowUserNamelabel.setObjectName("ShowUserNamelabel")
        self.userNameGridLayout.addWidget(self.ShowUserNamelabel, 0, 1, 1, 1)
        self.exitPushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.exitPushButton.setObjectName("exitPushButton")
        self.userNameGridLayout.addWidget(self.exitPushButton, 0, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.UserPageTab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, 99, 771, 401))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.UserPagegridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.UserPagegridLayout.setContentsMargins(0, 0, 0, 0)
        self.UserPagegridLayout.setObjectName("UserPagegridLayout")
        self.UserInfirmationGroupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.UserInfirmationGroupBox.setObjectName("UserInfirmationGroupBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.UserInfirmationGroupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(9, 19, 361, 361))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.InformationBoxGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.InformationBoxGridLayout.setContentsMargins(0, 0, 0, 0)
        self.InformationBoxGridLayout.setObjectName("InformationBoxGridLayout")
        self.Ratinglabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Ratinglabel.setObjectName("Ratinglabel")
        self.InformationBoxGridLayout.addWidget(self.Ratinglabel, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.InformationBoxGridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.RatingShowlabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.RatingShowlabel.setText("")
        self.RatingShowlabel.setObjectName("RatingShowlabel")
        self.InformationBoxGridLayout.addWidget(self.RatingShowlabel, 0, 1, 1, 1)
        self.UserPagegridLayout.addWidget(self.UserInfirmationGroupBox, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(9, 19, 361, 361))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.ActiveOrdergridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.ActiveOrdergridLayout.setContentsMargins(0, 0, 0, 0)
        self.ActiveOrdergridLayout.setObjectName("ActiveOrdergridLayout")
        self.activeOrdersScrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget_6)
        self.activeOrdersScrollArea.setWidgetResizable(True)
        self.activeOrdersScrollArea.setObjectName("activeOrdersScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 357, 357))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.activeOrdersScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.ActiveOrdergridLayout.addWidget(self.activeOrdersScrollArea, 0, 0, 1, 1)
        self.UserPagegridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.mainWindowTabWidget.addTab(self.UserPageTab, "")
        self.SearchTab = QtWidgets.QWidget()
        self.SearchTab.setObjectName("SearchTab")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.SearchTab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 751, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.ParametrSearchGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.ParametrSearchGridLayout.setContentsMargins(0, 0, 0, 0)
        self.ParametrSearchGridLayout.setObjectName("ParametrSearchGridLayout")
        self.SubjectLabel = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.SubjectLabel.setObjectName("SubjectLabel")
        self.ParametrSearchGridLayout.addWidget(self.SubjectLabel, 0, 0, 1, 1)
        self.newOrederPushButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.newOrederPushButton.setObjectName("newOrederPushButton")
        self.ParametrSearchGridLayout.addWidget(self.newOrederPushButton, 0, 3, 1, 1)
        self.SetSubjectcomboBox = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.SetSubjectcomboBox.setObjectName("SetSubjectcomboBox")
        self.ParametrSearchGridLayout.addWidget(self.SetSubjectcomboBox, 0, 1, 1, 1)
        self.startSearctPushButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.startSearctPushButton.setObjectName("startSearctPushButton")
        self.ParametrSearchGridLayout.addWidget(self.startSearctPushButton, 0, 2, 1, 1)
        self.orderOdlabel = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.orderOdlabel.setObjectName("orderOdlabel")
        self.ParametrSearchGridLayout.addWidget(self.orderOdlabel, 1, 0, 1, 1)
        self.openOrderPushButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.openOrderPushButton.setObjectName("openOrderPushButton")
        self.ParametrSearchGridLayout.addWidget(self.openOrderPushButton, 1, 2, 1, 1)
        self.orderIdLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.orderIdLineEdit.setMaxLength(200)
        self.orderIdLineEdit.setObjectName("orderIdLineEdit")
        self.ParametrSearchGridLayout.addWidget(self.orderIdLineEdit, 1, 1, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.SearchTab)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(9, 99, 751, 391))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.resultsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.resultsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.resultsGridLayout.setObjectName("resultsGridLayout")
        self.mainWindowTabWidget.addTab(self.SearchTab, "")
        self.gridLayout.addWidget(self.mainWindowTabWidget, 0, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainWindowTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UserNamelabel.setText(_translate("MainWindow", "UserName"))
        self.exitPushButton.setText(_translate("MainWindow", "Exit"))
        self.UserInfirmationGroupBox.setTitle(_translate("MainWindow", "Information"))
        self.Ratinglabel.setText(_translate("MainWindow", "Rating"))
        self.label_10.setText(_translate("MainWindow", "/10"))
        self.groupBox.setTitle(_translate("MainWindow", "Active orders"))
        self.mainWindowTabWidget.setTabText(self.mainWindowTabWidget.indexOf(self.UserPageTab), _translate("MainWindow", "UserPage"))
        self.SubjectLabel.setText(_translate("MainWindow", "Subject"))
        self.newOrederPushButton.setText(_translate("MainWindow", "New order"))
        self.startSearctPushButton.setText(_translate("MainWindow", "Search"))
        self.orderOdlabel.setText(_translate("MainWindow", "OrderId                   "))
        self.openOrderPushButton.setText(_translate("MainWindow", "OpenOrderPage"))
        self.mainWindowTabWidget.setTabText(self.mainWindowTabWidget.indexOf(self.SearchTab), _translate("MainWindow", "Search"))


class mainWindowController(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainWindowController, self).__init__(parent)
        self.setupUi(self)
        self.newOrederPushButton.clicked.connect(self.newOrederPushButton_clicked)
        self.startSearctPushButton.clicked.connect(self.searchPushButton_clicked)

    @QtCore.pyqtSlot()
    def newOrederPushButton_clicked(self):
        newOrderDialog = newOrderPageController()#QtWidgets.QDialog()
        #ui = NewOrderUi()
        #ui.setupUi(newOrderDialog)
        newOrderDialog.exec_()

        #print(ui.SetPricelineEdit.text())
        #self.newOrderWin = newOrderPageController()
    @QtCore.pyqtSlot()
    def searchPushButton_clicked(self):
        print("searchPushButton_clicked")
        '''self.startSearctPushButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.startSearctPushButton.setObjectName("startSearctPushButton")
        self.ParametrSearchGridLayout.addWidget(self.startSearctPushButton, 0, 2, 1, 1)'''
        #self.openOrderButton = QtWidgets.QPushButton("open order")
        #self.resultsGridLayout.addWidget(self.openOrderButton, 0, 2, 1, 1)
        #self.newOrderWin.show()

        #print(self.windowAdd)

