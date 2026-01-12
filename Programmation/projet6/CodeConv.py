from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication,QMessageBox
from pickle import load,dump
eur = dict(n1=int,cv=str)

def Ajouter():
    n = w.nn.text()
    if(not n.isdecimal() or n==""):
        QMessageBox.critical(w,"erreur","Veuillez saisir un entier n>0 .")
    f = open("Nombres.txt","a")
    f.write(n+'\n')
    f.close()
    
def Afficher1():
    f = open("Nombres.txt","r")
    n = f.readline()
    while(n!=""):
        w.list.addItem(n)
        n = f.readline()
    f.close()

def Effacer():
    w.list.clear()

def conv(n,b):
    ch = "0123456789ABCDEF"
    res = ""
    while(n>0):
        r = n%b
        n = n//b
        res =ch[r] +res
    return res

def Afficher2():
    e = dict(eur)
    b = w.combo.currentText()
    if(w.combo.currentText()=="..."):
        QMessageBox.critical(w,"erreur","Veuillez choisir une base.")
    else:
        f = open("Conv.dat","wb")
        f1 = open("Nombres.txt","r")
        n = f1.readline()
        while(n!=""):
            e["n1"] = int(n[0:len(n)-1])
            e["cv"] = conv(e["n1"],int(b))
            dump(e,f)
            n = f1.readline()
        f.close()
        f1.close()
        i=0
        f = open("Conv.dat","rb")
        eof = False
        while(not eof):
            try:
                e = load(f)
                print(e["n1"],e["cv"])
                w.tab.insertRow(i)
                w.tab.setItem(i, 0, QTableWidgetItem(str(e["n1"])))
                w.tab.setItem(i, 1, QTableWidgetItem(str(e["cv"])))
                i=i+1
            except:
                eof = True
        f.close()
    

def Fermer():
    w.close()

#---------Programme principale---------

app = QApplication([])
w = loadUi("InterfaceConv.ui")
w.show()
w.ajou.clicked.connect(Ajouter)
w.clear.clicked.connect(Effacer)
w.quit.clicked.connect(Fermer)
w.afftab.clicked.connect(Afficher2)
w.afflist.clicked.connect(Afficher1)
app.exec_()