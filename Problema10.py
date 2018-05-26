import numpy as np
import matplotlib.pyplot as plt



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