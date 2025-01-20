from tkinter import *


window = Tk()
window.title("Valeurs de tendance centrale et de dispersion")
window.minsize(720, 480)
icon = PhotoImage(master=window, file='cluster.png')
window.wm_iconphoto(True, icon)
f=("Helvetica", 18, "bold")

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


frameP1 = Frame(window)

labelP1 = Label(frameP1, text="Vatecedi", font=("Algerian", 25))
labelP1.pack(expand=True, fill=BOTH)
button1P1 = Button(frameP1, text="Variable discrète", font=f, command=page2)
button1P1.pack(fill=X, side=LEFT, padx=40)
button2P1= Button(frameP1, text="Variable continue", font=f, command=page3)
button2P1.pack(fill=X, side=RIGHT, padx=40)

frameP1.pack(expand=True, fill=BOTH)

frameP2 = Frame(window)

labelP2 = Label(frameP2, text="Valeurs de tendance centrale et de dispersion", font=("Algerian", 23))
subLabelP2= Label(frameP2, text="Variables discrètes", font=f)
labelP2.pack(expand=True, fill=BOTH)
subLabelP2.pack(expand=True, fill=BOTH)
buttonP2= Button(frameP2, text="Retour", font=f, command=page1)
buttonP2.pack(fill=X, side=BOTTOM, pady=40)

frameP3 = Frame(window)

labelP3 = Label(frameP3, text="Valeurs de tendance centrale et de dispersion", font=("Algerian", 23))
subLabelP3= Label(frameP3, text="Variables continues", font=f)
labelP3.pack(expand=True, fill=BOTH)
subLabelP3.pack(expand=True, fill=BOTH)
buttonP3= Button(frameP3, text="Retour", font=f, command=page1)
buttonP3.pack(fill=X, side=BOTTOM, pady=40)

window.mainloop()