from math import sqrt
from numpy import zeros


def entrerValeur(T, C):
    i = 0
    print("Entrer les valeurs de variable Xi puis les effectifs ni:")
    for i in range(0, C):
        y = 0
        while y == 0:
            x = input("Entrer X{}: ".format(i + 1))
            try:
                y = int(x)
            except:
                print("Erreur: la valeur n'est pas valide")
            else:
                T[0, i] = int(x)
    i = 0
    for i in range(0, C):
        y = 0
        while y == 0:
            x = input("Entrer l'effectif n{}: ".format(i + 1))
            try:
                y = int(x)
            except:
                print("Erreur: la valeur n'est pas valide")
            else:
                T[1, i] = int(x)


def afficherMatrice(T, C, a):
    j = 0
    for j in range(0, a):
        for i in range(0, C):
            print(T[j][i], end="   ")
        print()


def afficher(Ti):
    for elt in Ti:
        print(str(elt), end="   ")
    print()


def ECC(T, C, a):
    print("Effectifs cumulés croissants: ")
    T1 = zeros(C, int)
    T1[0] = T[a][0]
    for i in range(1, C):
        T1[i] = T1[i-1] + T[a][i]
    afficher(T1)
    return T1


def FCC(T1, C):
    print("Fréquences cumulées croissantes: ")
    T2 = zeros(C, float)
    for i in range(0, C):
        T2[i] = T1[i] / T1[C- 1]
    afficher(T2)
    return T2


def mode(T, C):
    y = T[0][0]
    x = T[1][0]
    i = 0
    for i in range(1, C):
        if T[1][i] > x:
            y = T[0][i]
    print("  Mode = " + str(y))
    return y


def somme(T, C, a):
    S = 0
    for i in range(0, C):
        S = S + T[a][i]
    return S


def moyenne(T, C, a):
    x = 0
    y = 0
    N = somme(T, C, a)
    for i in range(0, C):
        y = y + T[0][i]*T[1][i]
    x = y/N
    print("  Moyenne = " + str(x))
    return x


def quartile(T, T1, N, a):
    p = N * a
    i = 0
    while T1[i] < p:
        i = i + 1
    return T[0][i]


def variance(T, C, N, M):
    p = 0
    for i in range(0, C):
        p = p + T[1, i]*T[0, i]*T[0, i]
    V = (p/N) - M*M
    print("Variance = " + str(V))
    return V


def ecartType(V):
    E = sqrt(V)
    print("Ecart-type = " + str(E))
    return E


def intervalle_interquartile(Q1, Q3):
    I = Q3 - Q1
    print("Intervalle interquartile = " + str(I))
    return I

def etendu(T1, C):
    e = T1[C-1] - T1[0]
    print("Etendu = " + str(e))
    return e


def coef_variartion(E, M):
    coef = E / M
    print("Coefficient de variation = " + str(coef))
    return coef
