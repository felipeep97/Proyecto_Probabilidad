from typing import Any, Union

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# Ejercio 1
# a es la distribución inicial, P la matriz de transición, retorna la distribución de la n-esima variable de la sucesión
def cadena_de_markov(a, P, n):
    x = a
    for i in range(n):
        x = x @ P
    return x

def g(u, a):
    upperbound = 0
    for i in range(a.size):
        lowerbound = upperbound
        upperbound = lowerbound + a[i]
        if lowerbound < u <= upperbound:
            return i

def X_0(a):
    u = np.random.rand()
    return g(u, a)

def f(i, u, P):
    upperbound = 0
    for j in range(P.shape[0]):
        lowerbound = upperbound
        upperbound = lowerbound + P[i][j]
        if lowerbound < u <= upperbound:
            return j

def next(x, P):
    u = np.random.rand()
    return f(x, u, P)

#Ejercicio 8

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

#Calcula la matriz de transición para el problema 8
P = np.array([[]])
for i in range(9):
    x = np.array([])
    for j in range(9):
        x = np.append(x, transicion(i, j))
    P = np.append(P, x)
P = P.reshape(9, 9)
#print(P) #De-comentar esto para observar la matriz P en la consola


a = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]) #condicion inicial

def pi_i(i, N, a, P):
    tot = 0
    X = np.repeat(X_0(a), 100)
    for n in range(N):
        prob = 0. #P(X_n = i)
        for k in range(100):
            if X[k] == i:
                prob = prob +1.
            X[k] = next(X[k], P)
        prob = prob/100
        tot = tot + prob
    return float(tot)/N

#Con este fragmento se halló orginalmente pi, como es computacionalmente intenso y su resultado es aleatorio, se comentaron estas lineas y el valor obtenido de pi en la primera está horneado en el codigo
#pi = np.array([])
#for i in range(a.size):
#    pi = np.append(pi, round(pi_i(i, 1000, a, P), 3))
pi = np.array([0.17599556, 0.11364788, 0.14009092, 0.16568718, 0.17112309, 0.13563638, 0.07389974, 0.02429733, 0.00362192])


#Ejercio 9
import numpy as np
import matplotlib.pyplot as plt

X = np.repeat(X_0(a), 100)
Y = np.array([]) #Los resultados de las simulaciones se guardarán en este arreglo
for n in range(500):
    media = 0.0
    for i in range(100):
        media = media + float(X[i])
        X[i] = next(X[i], P)
    media = media/100
    Y = np.append(Y, media)

plt.plot(Y)
plt.show()



pi_f = 0
for i in range(9):
    pi_f = pi_f + i*pi[i]
print (pi_f)


#Ejercicio 10

Y = np.array([])
for i in range(500):
    x = X_0(a)
    for j in range(500):
        x = next(x, P)
    Y = np.append(Y, x)
plt.hist(Y, 9)
plt.show()



P500 = P
for i in range(499):
    P500 = P500@P
print (P500)



