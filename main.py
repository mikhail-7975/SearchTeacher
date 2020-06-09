from cancelOrder import *
from mainWindow import *
import database_func as db
from newOrder import *
from orderPage import  *
from loginWindowUI import *

#orderDataBase = db.database("orderDB")
#orderDataBase.insert("semanary OOD", "Stavro Evgenyevich", "bestsenno", "created")
#orderDataBase.insert("lektsyi OOD", "Miginsky", "bestsenno")
#orderDataBase.writeInFile("orderdb.txt")
#orderDataBase.readFromFile("orderdb.txt")

if __name__ == "__main__":
    import sys
    #orderDB = db.create_db("orderDB")
    #db.save_to_file(orderDB, "orderdb.txt")
    app = QtWidgets.QApplication(sys.argv)
    w1 = mainWindowController()  # = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    w1.show()  # MainWindow.show()
    app.exec_()
    print("closed1")
    #sys.exit(app.exec_())