from varDiscrete import *
from varContinue import *
import os
import sys
from tkinter import *

# En tête
header = "PROGRAMME"
header = header.center(60, "-")
print(header)

# Fenêtre
window = Tk()
window.title("Valeurs de tendance centrale et de dispersion")
window.minsize(720, 480)
icon = PhotoImage(master=window, file='cluster.png')
window.wm_iconphoto(True, icon)

#window.wm_iconbitmap('cluster.ico')

window.mainloop()

def div():
    h = ""
    h = h.center(40, "*")
    print(h)


# Choix du type de variables
print("Voulez vous réaliser une étude:")
print("1) Sur une variable discrète ?")
print("2) Sur une variable continue ?")
v = 0
while v == 0:
    x = input("Entrer votre choix(1 ou 2):  ")
    try:
        if x == "1" or x == "2":
            v = int(x)
        else:
            v == 0
    except:
        print("Erreur: la valeur n'est pas valide")
div()

# Nombre de variables
y = 0
while y == 0:
    x = input("Entrer le nombre de variables:  ")
    try:
        y = int(x)
    except:
        print("Erreur: la valeur n'est pas valide")
    else:
        C = int(x)

# Initialisation de la matrice
if v == 1:
    print("______VARIABLE DISCRETE______")
    T = zeros((2, C), int)
    entrerValeur(T, C)
    div()
    afficherMatrice(T, C, 2)
    N = somme(T, C, 1)
    print("N = " + str(N))
    T1 = ECC(T, C, 1)
    T2 = FCC(T1, C)
    div()
    print("VALEURS DE TENDANCE CENTRALE")
    Mo = mode(T, C)
    M = moyenne(T, C, 1)
    Me = quartile(T, T1, N, 0.5)
    print("  Mediane = " + str(Me))
    Q1 = quartile(T, T1, N, 0.25)
    print("  Q1 = " + str(Q1))
    Q2 = quartile(T, T1, N, 0.5)
    print("  Q2 = " + str(Q2))
    Q3 = quartile(T, T1, N, 0.75)
    print("  Q3 = " + str(Q3))
    div()
    print("VALEURS DE DISPERSION")
    V = variance(T, C, N, M)
    E = ecartType(V)
    Iq = intervalle_interquartile(Q1, Q3)
    e = etendu(T1, C)
    coef = coef_variartion(E, M)
else:
    print("______VARIABLE CONTINUE______")
    T = zeros((3, C), int)
    entrerValeurC(T, C)
    div()
    afficherMatrice(T, C, 3)
    N = somme(T, C, 2)
    print("N = " + str(N))
    div()
    T1 = ECC(T, C, 2)
    div()
    T2 = FCC(T1, C)
    div()
    print("VALEURS DE TENDANCE CENTRALE")
    tab = densite_frequence(T, C, N)
    cm = classe_modale(T, tab, C)
    Mo = modeC(T, tab, cm, C)
    M = moyenneC(T, C, 2)
    Me = quartileC(T, T1, T2, tab, N, C, 0.5)
    print("  Mediane = " + str(Me))
    Q1 = quartileC(T, T1, T2, tab, N, C, 0.25)
    print("  Q1 = " + str(Q1))
    Q2 = quartileC(T, T1, T2, tab, N, C, 0.5)
    print("  Q2 = " + str(Q2))
    Q3 = quartileC(T, T1, T2, tab, N, C, 0.75)
    print("  Q3 = " + str(Q3))
    div()
    print("VALEURS DE DISPERSION")
    V = varianceC(T, C, N, M)
    E = ecartType(V)
    Iq = intervalle_interquartile(Q1, Q3)
    e = etendu(T1, C)
    coef = coef_variartion(E, M)

div()
print("fin")

def restart_program():
    try:
        python_executable = sys.executable
        script_path = sys.argv[0]
        script_args = sys.argv[1:]
        os.execl(python_executable, python_executable, script_path, *script_args)
    except Exception as e:
        print(f"Erreur lors du redémarrage : {e}")
        sys.exit(1)

if __name__ == "__main__":
    user_input = input("Voulez-vous redémarrer le programme ? (oui/non) : ")
    if user_input.lower() == "oui":
        restart_program()
    else:
        print("Fin du programme.")
