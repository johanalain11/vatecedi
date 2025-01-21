from tkinter import *
from numpy import zeros


window = Tk()
window.title("Valeurs de tendance centrale et de dispersion")
window.minsize(720, 480)
icon = PhotoImage(master=window, file='cluster.png')
window.wm_iconphoto(True, icon)
f=("Helvetica", 18, "bold")
f2=("Helvetica", 15)
t1="Entrer le nombre de variables: "
nbVar = 0
i = 1
T = zeros((2, nbVar), int)

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
    y = nbVarEntry.get()
    try :
        nbVar = int(y)
        if nbVar <= 0 :
            raise ValueError
    except :
        nbVarEntry.config(bg='red', fg='white')
    else :
        nbVarValid.grid_forget()
        nbVarOk.grid(row=1, column=0, pady=10, padx=5, columnspan=2)
        nbVarEntry.config(text=" ", bg = "white")
        nbVarLabel.config(text="Entrer X[{}]: ".format(i))

def saveData(nbVar, T, i) :
    if i in range(2, nbVar+1) :
        i = i + 1
        c = nbVarEntry.get()
        T[0, i-2] = int(c)
        nbVarEntry.config(text=" ", bg="white")
        nbVarLabel.config(text="Entrer X[{}]: ".format(i))
    elif i == nbVar :
        nbVarOk.grid_forget()

    return i, T


# PREMIERE PAGE
frameP1 = Frame(window)

labelP1 = Label(frameP1, text="Vatecedi", font=("Algerian", 25))
subLabelP1= Label(frameP1, text="Valeurs de tendance centrale et de dispersion", font=f)
labelP1.pack(expand=True, fill=BOTH)
subLabelP1.pack(expand=True, fill=BOTH)
button1P1 = Button(frameP1, text="Variables discrètes", font=f, command=page2)
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
nbVarLabel.grid(row=0, column=0, pady=10, padx=5)
nbVarEntry = Entry(frameP22, textvariable=nbVar, font=f2, bg = "#defcfb")
nbVarEntry.grid(row=0, column=1, pady=10, padx=5)
nbVarValid = Button(frameP22, text="Valider", font=f2, command=valid)
nbVarValid.grid(row=1, column=0, pady=10, padx=5, columnspan=2)
nbVarOk = Button(frameP22, text="OK", font=f2, command=saveData(nbVar, T, i))
frameP22.pack(fill=X)

# Bouton Retour
buttonP2= Button(frameP2, text="Retour", font=f, command=page1)
buttonP2.pack(fill=X, side=BOTTOM, pady=40, padx=20)

# PAGE NUMERO 3
frameP3 = Frame(window)

labelP3 = Label(frameP3, text="Vatecedi", font=("Algerian", 23))
subLabelP3= Label(frameP3, text="Variables continues", font=f)
labelP3.pack(expand=True, fill=BOTH)
subLabelP3.pack(expand=True, fill=BOTH)
imageP3 = PhotoImage(file="Vatecedi2.png")
imgP3 = Label(frameP3, image=imageP3).pack(expand=True, fill=BOTH)
buttonP3= Button(frameP3, text="Retour", font=f, command=page1)
buttonP3.pack(fill=X, side=BOTTOM, pady=40, padx=20)

window.mainloop()