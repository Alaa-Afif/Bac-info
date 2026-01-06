from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox

def CalculScore():
    #finc1 cinc1

    sc = 0
    if(w.fc.isChecked()):
        sc+=2
    if(w.cc.isChecked()):
        sc+=2
    if(w.ordre.currentText()=='2'):
        sc+=3
    return sc

def Verif(cin,np):
    test = True
    if(not(len(cin) == 8 and cin.isdecimal()  and  "0"<=cin[0]<="1")):
        QMessageBox.critical(w,"erreur","N° CIN invalide.")
        test = False
    elif(np == "" or not verif_np(np)):
        QMessageBox.critical(w,"erreur","Vérifier votre Nom et Prénom")
        test = False
    return test


def Afficher():
    cin  = str(w.CIN.text())
    np  = str(w.NP.text())
    if(Verif(cin,np)):
        sc = CalculScore()
        cin = "CIN "+cin
        np  = "Nom Prénom : "+np
        ch = "Score : "+str(sc)
        w.res.addItem(cin)
        w.res.addItem(np)
        w.res.addItem(ch)



def verif_np(np):
    test = True;
    for i in range(0,len(np)):
        if not ("a"<=np[i].lower()<="z"or np[i] == " "):
            test = False
    return test


#---------Programme principale---------

app = QApplication([])
w = loadUi("InterfaceEval.ui")
w.show()
w.aff.clicked.connect(Afficher)
app.exec_()
