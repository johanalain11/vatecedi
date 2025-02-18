from numpy import zeros


def entrerValeurC(T, C):
    i = 0
    print("Entrer les valeurs de variable X[i], ensuite X[(i)+1] puis les effectifs ni:")
    for i in range(0, C):
        y = 0
        while y == 0:
            x = input("Entrer X[{}]: ".format(i + 1))
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
            x = input("Entrer X[({})+1]: ".format(i + 1))
            try:
                if int(x) > T[0, i]:
                    y = int(x)
                else:
                    y == 0
            except:
                print("Erreur: la valeur n'est pas valide")
            else:
                T[1, i] = int(x)
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
                T[2, i] = int(x)


def densite_frequence(T, C, N):
    tab = zeros((3, C), float)
    # Calcul des amplitudes
    for i in range(0, C):
        tab[0, i] = T[1, i] - T[0, i]
    # Calcul des fréquences
    for j in range(0, C):
        tab[1][j] = T[2, j]/N
    # Calcul des densités
    for k in range(0, C):
        tab[2, k] = tab[1, k] / tab[0, k]
    return tab


def classe_modale(T, tab, C):
    b = tab[2, 0]
    a = 0
    for i in range(1, C):
        if tab[2, i] > b:
            b = tab[2, i]
            a = i
    print("  Classe modale = [" + str(T[0, a]) + ";" + str(T[1, a]) + "[")
    return a


def modeC(T, tab, a, C):
    if a == 0:
        D1 = T[2, a]
        D2 = T[2, a] - T[2, a + 1]
    elif a == C-1:
        D1 = T[2, a] - T[2, a-1]
        D2 = T[2, a]
    else:
        D1 = T[2, a] - T[2, a-1]
        D2 = T[2, a] - T[2, a+1]
    Mo = T[0, a] + tab[0, a]*(D1 / (D1 + D2))
    print("  Mode = " + str(Mo))
    return Mo


def somme(T, C, a):
    S = 0
    for i in range(0, C):
        S = S + T[a][i]
    return S


def moyenneC(T, C, a):
    x = 0
    y = 0
    N = somme(T, C, a)
    for i in range(0, C):
        y = y + T[2][i] * (T[0][i] + T[1][i])/2
    x = y/N
    print("  Moyenne = " + str(x))
    return x


def quartileC(T, T1, T2, tab, N, C, a):
    p = N*a
    i = 0
    for j in range(0, C):
        if T1[i] < p:
            i = j
    if i == 0:
        F = 0
    else:
        F = T2[i-1]
    q = T[0, i] + tab[0, i]*((a - F) / tab[1, i])
    return q


def varianceC(T, C, N, M):
    p = 0
    for i in range(0, C):
        p = p + T[2, i]*((T[0, i] + T[1, i])/2)*((T[0, i] + T[1, i])/2)
    V = (p/N) - M*M
    print("Variance = " + str(V))
    return V
