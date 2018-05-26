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