import random

class element:
    subject = ""
    author = ""
    whoRequired = ""
    price = ""
    status = ""
    def __init__(self, _subject: str, _author: str, _whoReq: str, _price: str, _status: str):
        self.subject = _subject
        self.author = _author
        self.whoRequired = _whoReq
        self.price = _price
        self.status = _status

class database:
    data = {}
    stringsOfTable = []
    db_name = ""
    odrerCounter = 0
    def __init__(self, name):
        self.db_name = name

    def insert(self, subject, author, whoReq, price, status,  id=-1):
        self.odrerCounter += 1
        info = element(subject, author, whoReq, price, status)
        #dict.update(self.odrerCounter, info)
        if (id == -1):
            self.data[random.randint(0, 1000000)] = info
        else:
            self.data[id] = info

    def writeInFile(self, fileName):
        f = open(fileName, "w")
        for key in self.data:
            f.write(str(key) + "\t" + str(self.data[key].subject) + "\t" + str(str(self.data[key].author)) +
                    "\t" + str(str(self.data[key].whoRequired)) + "\t" + str(self.data[key].price) + "\t" + str(self.data[key].status) + "\n")
        f.close()

    def readFromFile(self, fileName):
        f = open(fileName, "r")
        strings = f.read().split("\n")
        self.stringsOfTable = strings
        print(strings)
        for i in strings:
            try:
                _id, subjectName, teacherName, price = i.split("\t")
                self.insert(subjectName, teacherName, price, id=_id)
            except Exception:
                print("WTF???")
        f.close()

    def searchInFile(self, fileName, stringToSearch):
        f = open(fileName, "r")
        strings = f.read().split("\n")
        self.stringsOfTable = strings
        result = ""
        for i in self.stringsOfTable:
            #S.find(str, [start],[end])
            if(i.find(stringToSearch) != -1):
                result += (i + '\n')
        f.close()
        return result

    def returnWithId(self, id):
        print(int(id))
        print(id)
        print(type(id))
        try:
            result = self.data[int(id)]

        except Exception:
            result = element("0", "0", "0", "0", "0")

        return result

    def modify(self, fileName, id, _subject: str, _author: str, _whoReq: str, _price: str, _status: str):
        self.readFromFile(fileName)
        self.data[id] = element(_subject, _author, _whoReq, _price, _status)
        self.writeInFile(fileName)

