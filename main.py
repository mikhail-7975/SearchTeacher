from cancelOrder import *
from mainWindow import *
from newOrder import *
from orderPage import  *
from loginWindowUI import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = loginWindowController()# = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    w.show()#MainWindow.show()
    app.exec_()
    print("closed")
    app1 = app
    w1 = orderPageController()  # = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    w1.show()  # MainWindow.show()
    app1.exec_()
    print("closed1")
    #sys.exit(app.exec_())