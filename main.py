from cancelOrder import *
from mainWindow import *
from newOrder import *
from orderPage import  *
from loginWindowUI import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w1 = mainWindowController()  # = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    w1.show()  # MainWindow.show()
    app.exec_()
    print("closed1")
    #sys.exit(app.exec_())