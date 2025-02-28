import os
import sys
from tkinter import *
from tkinter.ttk import Treeview

from modules.varDiscrete import *
from modules.varContinue import *


window = Tk()
window.title("Valeurs de tendance centrale et de dispersion")
window.minsize(720, 480)
icon = PhotoImage(master=window, file='images/cluster.png')
window.wm_iconphoto(True, icon)

f=("Helvetica", 18, "bold")
f2=("Helvetica", 15)
t1="Entrer le nombre de variables: "
i = 0
boolean = False
T = zeros((3, 30), int)
a = 0
nbVar: int = 0
vartype = ""

def page1():
    os.execv(sys.executable, ['python'] + sys.argv)

def page2():
    global vartype
    vartype = "discrete"
    frameP2.pack(fill=BOTH, expand=True)
    frameP1.pack_forget()
    frameP3.pack_forget()

def page3():
    global vartype
    vartype = "continue"
    frameP3.pack(fill=BOTH, expand=True)
    frameP2.pack_forget()
    frameP1.pack_forget()

# Fonction qui enregistre le nombre de variables
def valid():
    global nbVar, i, boolean, a, vartype
    if nbVarValid.cget("text") == "Valider" or nbVarValid2.cget("text") == "Valider":
        if vartype == "discrete" :
            y = nbVarEntry.get()
        else :
            y = nbVarEntry2.get()
        print("**** Bouton Valider {} cliqué".format(vartype))
        try :
            nbVar = int(y)
            if nbVar <= 0 :
                raise ValueError
        except :
            nbVarEntry.config(bg='red', fg='white')
            nbVarEntry2.config(bg='red', fg='white')
        else :
            print("a = " + str(a))
            print("i = " + str(i))
            print("nbVar = ", nbVar)
            nbVarValid.config(text="OK")
            nbVarValid2.config(text="OK")
            if vartype == "discrete" :
                nbVarLabel.config(text="Entrer X[{}]: ".format(i+1))
                nbVarEntry.delete(0, END)
                nbVarEntry.config(bg = "white", fg = "black")
            else :
                nb1.grid(row=0, column=1, padx=3)
                nbVarEntry2.grid(row=0, column=2, pady=10, padx=5)
                nbVarEntry2.config(width=6)
                nb2.grid(row=0, column=3, padx=3)
                nbVarEntry3.grid(row=0, column=4, pady=10, padx=5)
                nb3.grid(row=0, column=5, padx=3)
                nbVarValid2.config(text="OK")
                nbVarValid.config(text="OK")
                nbVarEntry2.delete(0, END)
                nbVarEntry2.config(bg = "#defcfb", fg = "black")
                nbVarLabel2.config(text="Entrer [x{}; y{}] : ".format(i+1, i+1))

    elif nbVarValid.cget("text") == "OK" or nbVarValid2.cget("text") == "OK" :
        saveData()
        if (i == nbVar) & (boolean == False) :
            boolean = True
            i = 0
            a = 1
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
            if vartype == "continue" :
                nbVarLabel2.config(text="Entrer n[{}]: ".format(i+1))
                nb1.destroy()
                nb2.destroy()
                nb3.destroy()
                nbVarEntry3.grid_forget()
                nbVarEntry2.grid(row=0, column=1, pady=10, padx=5)
                nbVarEntry2.config(width=12)
        elif (i < nbVar-1) & boolean == True :
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
            if vartype == "continue" :
                nbVarLabel2.config(text="Entrer n[{}]: ".format(i+1))
        elif (i == nbVar-1) & boolean == True :
            nbVarValid.config(text="Calculer")
            nbVarValid2.config(text="Calculer")
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
            if vartype == "continue" :
                nbVarLabel2.config(text="Entrer n[{}]: ".format(i+1))
    elif nbVarValid.cget("text") == "Calculer":
        saveData()
        if vartype == "discrete" :
            nbVarEntry.config(bg = "black", fg = "white")
            nbVarLabel.config(text="Résultats", bg='#defcfb')
            afficherMatrice(T, nbVar, 2)
            nbVarValid.config(state=DISABLED)
        else:
            nbVarEntry2.config(bg = "black", fg = "white")
            nbVarLabel2.config(text="Résultats", bg='#defcfb')
            afficherMatrice(T, nbVar, 3)
            nbVarValid2.config(state=DISABLED)
        afficher_tableau()


def saveData() :
    global T, i, a, nbVar, vartype
    print("***** Bouton OK cliqué")
    if i in range(0, nbVar) :

        if vartype == "discrete" :
            c = nbVarEntry.get()
            print("Valeur entrée: " + c)
            T[a, i] = int(c)
            nbVarEntry.delete(0, END)
            if a == 0  :
                nbVarLabel.config(text="Entrer X[{}]: ".format(i+1))
            nbVarValid.flash()
        else :  # Si c'est une variable continue
            if a == 0:
                d = nbVarEntry2.get()
                e = nbVarEntry3.get()
                T[a, i] = int(d)
                T[a+1, i] = int(e)
                print("Valeur entrée x : " + d)
                print("Valeur entrée y : " + e)
            else:
                d = nbVarEntry2.get()
                T[2, i] = int(d)
                print("Valeur entrée n : " + d)
                afficherMatrice(T, nbVar, 3)
            nbVarEntry2.delete(0, END)
            nbVarEntry3.delete(0, END)
            if a == 0  :
                nbVarLabel2.config(text="Entrer [x{}; y{}] : ".format(i+1, i+1))
            nbVarValid2.flash()

        i = i + 1
        print("a = " + str(a))
    else :
        print("Valeur non entrée")
        nbVarValid.config(text="Calculer")
    print("i = " + str(i))

def afficher_tableau():
    global T, nbVar, colonnes, colonnes2, vartype
    if vartype == "discrete":
        for col in colonnes:
            tableau.heading(col, text=col)
            tableau.column(col, width=100, anchor="center")

        k = 0
        for lignes in list(zip(*T)) :
            if k < nbVar:
                tableau.insert("", END, values=lignes)
                k = k+1

        calcul_statistique()
        tableau.pack(fill=BOTH, expand=True)
    else:
        for col in colonnes2:
            tableau2.heading(col, text=col)
            tableau2.column(col, width=100, anchor="center")

        k = 0
        for lignes in list(zip(*T)) :
            if k < nbVar:
                tableau2.insert("", END, values=lignes)
                k = k+1

        calcul_statistique()
        tableau2.pack(fill=BOTH, expand=True)

def calcul_statistique():
    global T, nbVar, tableau, vartype
    if vartype == "discrete":
        N = somme(T, nbVar, 1)
        T1 = ECC(T, nbVar, 1)
        T2 = FCC(T1, nbVar)
        print("VALEURS DE TENDANCE CENTRALE")
        Mo = mode(T, nbVar)
        M = moyenne(T, nbVar, 1)
        Me = quartile(T, T1, N, 0.5)
        Q1 = quartile(T, T1, N, 0.25)
        Q2 = quartile(T, T1, N, 0.5)
        Q3 = quartile(T, T1, N, 0.75)
        V = variance(T, nbVar, N, M)
    else:
        N = somme(T, nbVar, 2)
        T1 = ECC(T, nbVar, 2)
        T2 = FCC(T1, nbVar)
        print("VALEURS DE TENDANCE CENTRALE")
        tab = densite_frequence(T, nbVar, N)
        cm = classe_modale(T, tab, nbVar)
        Mo = modeC(T, tab, cm, nbVar)
        M = moyenneC(T, nbVar, 2)
        Me = quartileC(T, T1, T2, tab, N, nbVar, 0.5)
        Q1 = quartileC(T, T1, T2, tab, N, nbVar, 0.25)
        Q2 = quartileC(T, T1, T2, tab, N, nbVar, 0.5)
        Q3 = quartileC(T, T1, T2, tab, N, nbVar, 0.75)
        V = varianceC(T, nbVar, N, M)
    t1 = " ".join(map(str, T1))
    t2 = " ".join(map(str, T2))
    print("VALEURS DE DISPERSION")
    E = ecartType(V)
    Iq = intervalle_interquartile(Q1, Q3)
    e = etendu(T1, nbVar)
    coef = coef_variation(E, M)
    C = "TENDANCES CENTRALES"
    D = "DE DISPERSION"
    t = "--------------"
    valeurs = [
        ("--------------", t),
        ("VALEURS DE ", C),
        ("Somme", N),
        ("Effectifs cumulés", T1),
        ("Fréquences cumulées", T2),
        ("Mode", Mo),
        ("Moyenne", M),
        ("Médiane", Me),
        ("1er quartile", Q1),
        ("2e quartile", Q2),
        ("3e quartile", Q3),
        ("--------------", t),
        ("VALEURS DE ", D),
        ("Variance", V),
        ("Écart-Type", E),
        ("Intervalle Interquartile", Iq),
        ("Étendue", e),
        ("Coef de Variation", coef)
    ]
    # Ajout des lignes au tableau Treeview
    if vartype == "discrete" :
        for idx, (nom, valeur) in enumerate(valeurs, start=0):
            tableau.insert("", "end", values=(nom, valeur))
    else:
        for idx, (nom, valeur) in enumerate(valeurs, start=0):
            tableau2.insert("", "end", values=(nom, valeur))


# PREMIERE PAGE
frameP1 = Frame(window)

labelP1 = Label(frameP1, text="Vatecedi", font=("Algerian", 25))
subLabelP1= Label(frameP1, text="Valeurs de tendance centrale et de dispersion", font=f)
labelP1.pack(expand=True, fill=BOTH)
subLabelP1.pack(expand=True, fill=BOTH)
button1P1 = Button(frameP1, text="Variables discrètes", font=f, command=page2, relief="sunken")
button1P1.pack(fill=BOTH, side=LEFT, pady=40, padx=20)
button2P1= Button(frameP1, text="Variables continues", font=f, command=page3)
button2P1.pack(fill=BOTH, side=RIGHT, pady=40, padx=20)

frameP1.pack(expand=True, fill=BOTH)

# PAGE NUMERO 2
frameP2 = Frame(window)

labelP2 = Label(frameP2, text="Vatecedi", font=("Algerian", 23))
subLabelP2= Label(frameP2, text="Variables discrètes", font=f)
labelP2.pack(expand=True, fill=BOTH)
subLabelP2.pack(expand=True, fill=BOTH)
imageP2 = PhotoImage(file="images/Vatecedi.png")
imgP2 = Label(frameP2, image=imageP2).pack(expand=True, fill=BOTH)
s1= SEPARATOR

#frame n°1
frameP22 = Frame(frameP2)
nbVarLabel = Label(frameP22, text=t1, font=f2)
nbVarLabel.grid(row=0, column=0, pady=10, padx=(50, 5))
nbVarEntry = Entry(frameP22, font=f2, bg = "#defcfb")
nbVarEntry.grid(row=0, column=1, pady=10, padx=5)
nbVarValid = Button(frameP22, text="Valider", font=f2, command=valid)
nbVarValid.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
frameP22.pack(fill=X)

#frame n°2
frameP23 = Frame(frameP2)
frameP23.pack(fill="both", expand=True, padx=10, pady=10)
colonnes = ("Xi", "ni")
tableau = Treeview(frameP23, columns=colonnes, show="headings")

# Bouton Retour
buttonP2= Button(frameP2, text="Retour", font=f, command=page1, relief="sunken")
buttonP2.pack(fill=X, side=BOTTOM, pady=40, padx=20)

# PAGE NUMERO 3
frameP3 = Frame(window)

labelP3 = Label(frameP3, text="Vatecedi", font=("Algerian", 23))
subLabelP3= Label(frameP3, text="Variables continues", font=f)
labelP3.pack(expand=True, fill=BOTH)
subLabelP3.pack(expand=True, fill=BOTH)
imageP3 = PhotoImage(file="images/Vatecedi2.png")
imgP3 = Label(frameP3, image=imageP3).pack(expand=True, fill=BOTH)
buttonP3= Button(frameP3, text="Retour", font=f, command=page1, relief="sunken")
buttonP3.pack(fill=X, side=BOTTOM, pady=40, padx=20)

#frame n°1
frameP32 = Frame(frameP3)
nbVarLabel2 = Label(frameP32, text=t1, font=f2)
nbVarLabel2.grid(row=0, column=0, pady=10, padx=(50, 5))

nbVarEntry2 = Entry(frameP32, font=f2, bg= "#defcfb")
nbVarEntry2.grid(row=0, column=1, pady=10, padx=5)

nbVarEntry3 = Entry(frameP32, font=f2, bg= "#defcfb")
nbVarEntry3.config(width=6 )

nb1 = Label(frameP32, text="[", font=f2)
nb2 = Label(frameP32, text=";", font=f2)
nb3 = Label(frameP32, text="]", font=f2)

nbVarValid2 = Button(frameP32, text="Valider", font=f2, command=valid)
nbVarValid2.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
frameP32.pack(fill=X)

#frame n°2
frameP33 = Frame(frameP3)
frameP33.pack(fill="both", expand=True, padx=10, pady=10)
colonnes2 = ("Xi", "Yi", "ni")
tableau2 = Treeview(frameP33, columns=colonnes2, show="headings")

window.mainloop()