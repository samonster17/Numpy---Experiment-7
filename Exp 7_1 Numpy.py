import numpy as np
x = np.random.random((5,5))
m = np.mean(x)
y = np.std(x)

z = (x-m)/(y)

np.save('X_normallized.npy', z)
