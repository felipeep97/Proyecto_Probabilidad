import numpy as np

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
    x = 0
    upperbound = 0
    for j in range(P.shape[0]):
        lowerbound = upperbound
        upperbound = lowerbound + P[i][j]
        if lowerbound < u <= upperbound:
            x = x + j
    return x

def next(x, P):
    u = np.random.rand()
    return f(x, u, P)

