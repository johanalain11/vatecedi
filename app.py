from tkinter import *
from tkinter.ttk import Treeview

from varDiscrete import *
from varContinue import *


window = Tk()
window.title("Valeurs de tendance centrale et de dispersion")
window.minsize(720, 480)
icon = PhotoImage(master=window, file='cluster.png')
window.wm_iconphoto(True, icon)

f=("Helvetica", 18, "bold")
f2=("Helvetica", 15)
t1="Entrer le nombre de variables: "
i = 0
boolean = False
T = zeros((2, 30), int)
a = 0
nbVar: int = 0

def page1():
    frameP1.pack(fill=BOTH, expand=True)
    frameP2.pack_forget()
    frameP3.pack_forget()

def page2():
    frameP2.pack(fill=BOTH, expand=True)
    frameP1.pack_forget()
    frameP3.pack_forget()

def page3():
    frameP3.pack(fill=BOTH, expand=True)
    frameP2.pack_forget()
    frameP1.pack_forget()

# Fonction qui enregistre le nombre de variables
def valid():
    global nbVar, i, boolean, a
    if nbVarValid.cget("text") == "Valider":
        y = nbVarEntry.get()
        print("**** Bouton Valider cliqué")
        try :
            nbVar = int(y)
            if nbVar <= 0 :
                raise ValueError
        except :
            nbVarEntry.config(bg='red', fg='white')
        else :
            print("a = " + str(a))
            print("i = " + str(i))
            print("nbVar = ", nbVar)
            nbVarValid.config(text="OK")
            nbVarEntry.delete(0, END)
            nbVarEntry.config(bg = "white", fg = "black")
            nbVarLabel.config(text="Entrer X[{}]: ".format(i+1))
    elif nbVarValid.cget("text") == "OK":
        saveData()
        if (i == nbVar) & (boolean == False) :
            boolean = True
            i = 0
            a = 1
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
        elif (i < nbVar-1) & boolean == True :
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
        elif (i == nbVar-1) & boolean == True :
            nbVarValid.config(text="Calculer")
            nbVarLabel.config(text="Entrer n[{}]: ".format(i+1))
    elif nbVarValid.cget("text") == "Calculer":
        saveData()
        nbVarEntry.config(bg = "black", fg = "white")
        nbVarLabel.config(text="Résultats", bg='#defcfb')
        afficherMatrice(T, nbVar, 2)
        afficher_tableau()
        nbVarValid.config(state=DISABLED)


def saveData() :
    global T, i, a, nbVar
    print("**** Bouton OK cliqué")
    if i in range(0, nbVar) :
        c = nbVarEntry.get()
        T[a, i] = int(c)
        nbVarEntry.delete(0, END)
        print("a = " + str(a))
        print("Valeur entrée: " + c)
        # nbVarEntry.config(bg="white", fg = "black")
        i = i + 1
        if a == 0  :
        #else:
            nbVarLabel.config(text="Entrer X[{}]: ".format(i+1))
        nbVarValid.flash()
    else :
        print("Valeur non entrée")
        nbVarValid.config(text="Calculer")
    print("i = " + str(i))

def afficher_tableau():
    global T, nbVar
    colonnes = ("Xi", "ni")
    tableau = Treeview(frameP23, columns=colonnes, show="headings")
    for col in colonnes:
        tableau.heading(col, text=col)
        tableau.column(col, width=100, anchor="center")

    k = 0
    for lignes in list(zip(*T)) :
        tableau.insert("", END, values=lignes)

    tableau.pack(fill=BOTH, expand=True)


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
imageP2 = PhotoImage(file="Vatecedi.png")
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

# Bouton Retour
buttonP2= Button(frameP2, text="Retour", font=f, command=page1, relief="sunken")
buttonP2.pack(fill=X, side=BOTTOM, pady=40, padx=20)

# PAGE NUMERO 3
frameP3 = Frame(window)

labelP3 = Label(frameP3, text="Vatecedi", font=("Algerian", 23))
subLabelP3= Label(frameP3, text="Variables continues", font=f)
labelP3.pack(expand=True, fill=BOTH)
subLabelP3.pack(expand=True, fill=BOTH)
imageP3 = PhotoImage(file="Vatecedi2.png")
imgP3 = Label(frameP3, image=imageP3).pack(expand=True, fill=BOTH)
buttonP3= Button(frameP3, text="Retour", font=f, command=page1, relief="sunken")
buttonP3.pack(fill=X, side=BOTTOM, pady=40, padx=20)

window.mainloop()