from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication,QMessageBox
from numpy import array


def verif(n):
    if(not n.isdecimal()):
        return False
    elif(not 2<=int(n)<=10):
        return False
    return True

def fact(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res

def combo(p,n):
    return fact(n)//(fact(p)*fact(n-p))


def triang(n,t):
    for i  in range(n):
        for j in range(i+1):
            t[i][j] = combo(j,i)


def Afficher():
    if(not verif(w.name.text())):
        QMessageBox.critical(w,"erreur","Veuillez sasir une n valide .")
    else:
        n = int(w.name.text())
        t = array([[int()]*n]*n)
        triang(n,t)
        w.tab.setRowCount(n)
        w.tab.setColumnCount(n)
        for i in range(0,n):
            for j in range(i+1):
                w.tab.setItem(i,j,QTableWidgetItem(str(t[i][j])))


app = QApplication([])
w = loadUi("pascal.ui")
w.show()
w.aff.clicked.connect(Afficher) 
app.exec_()
