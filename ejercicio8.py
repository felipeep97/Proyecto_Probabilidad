import numpy as np
import scipy.special as sp


# Retorna la probabilidad de obtener un resultado de k de una distribución binomial con parametros (n, p), por defecto (10, 0.4)
def binom(k, n=10, p=0.4):
    return sp.comb(n, k)*(p**k)*(1-p)**(n-k)


# Retorna la entrada i,j de la matriz de transición en el ejercicio 8
def transicion(i, j):
    if i <= 3:
        if j == 0:
            return binom(8) + binom(9) + binom(10)
        else:
            return binom(8 - j)
    else:
        if j == 0:
            x = 0
            for k in range(i, 11):
                x = x + binom(k)
            return x
        else:
            return binom(i - j)


P = np.array([[]]) #matriz de transición
for i in range(9):
    x = np.array([])
    for j in range(9):
        x = np.append(x, transicion(i, j))
    P = np.append(P, x)
P = P.reshape(9, 9)
print(P)