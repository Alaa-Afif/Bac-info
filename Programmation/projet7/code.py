from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication,QMessageBox
from pickle import load,dump
eur = dict(mat = str,np = str,ge = str,tit=str)
def verif(c):
    test = True
    ch = "0123456789ABCDEF"
    for i in range(len(c)):
        if(ch.find(c[i])==-1):
            test = False
    return test
def verif1(c):
    test = True
    for i in range(len(c)):
        if(not("A"<=c[i]<="Z" or "a"<=c[i]<="z" or c[i]==" " )):
            test = False
    return test

def Ajouter():
    if(not verif(w.ma.text())):
        QMessageBox.critical(w,"erreur","Veuillez sasir le bon matricule.")
    elif(not verif1(w.np.text())):
        QMessageBox.critical(w,"erreur","Veuillez sasir le bon nom prenom.")
    elif(not(w.gm.isChecked() or w.gf.isChecked())):
        QMessageBox.critical(w,"erreur","Veuillez selectionnez le genre")
    else:
        e = eur
        e["mat"] = w.ma.text()
        e["np"] = w.np.text()
        e["ge"]=""
        if(w.gm.isChecked()):
            e["ge"] = "Masculin"
        else:
            e["ge"] = "Feminin"
        e["tit"] = "Non"
        if(w.tit.isChecked()):
            e["tit"] = "Oui"
        f = open("Employés.dat","ab")
        dump(e,f)
        f.close()
        QMessageBox.critical(w,"success","Ajouter par succés")
        
        
def Effacer():
    w.ma.clear()
    w.np.clear()
def AffEmp():
    f = open("Employés.dat","rb")
    eof = False
    i=0
    while(not eof):
        try:
            e = load(f)
            w.tab.insertRow(i)
            w.tab.setItem(i,0,QTableWidgetItem(e["mat"]))
            w.tab.setItem(i,1,QTableWidgetItem(e["np"]))
            w.tab.setItem(i,2,QTableWidgetItem(e["ge"]))
            w.tab.setItem(i,3,QTableWidgetItem(e["tit"]))
            i+=1
        except:
            eof = True
    f.close()
    
def conv(c):
    ch = "0123456789ABCDEF"
    p=1
    res = 0
    for i in range(len(c)):
        j = len(c)-i-1
        res+= ch.find(c[j])*p
        p*=16
    return res

def div13(n):
    if(len(str(n))==2):
        return n%13==0
    else:
        return div13((n//10) + (n%10)*4)

def AffDec():
    f = open("Employés.dat","rb")
    eof = False
    while(not eof):
        try:
            e = load(f)
            if(div13(int(conv(e["mat"])))):
                ch = str(e["mat"])+" : "+str(e["np"])
                w.list.addItem(ch)
        except:
            eof = True
    f.close()
def Fermer():
    w.close()
# -----------programme_principale-----------

app = QApplication([])
w = loadUi("interfaceEmploy.ui")
w.show()
w.ajou.clicked.connect(Ajouter)
w.eff.clicked.connect(Effacer)
w.quit.clicked.connect(Fermer)
w.affemp.clicked.connect(AffEmp)
w.affdec.clicked.connect(AffDec)
app.exec_()