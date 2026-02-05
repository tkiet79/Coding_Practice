import numpy as np

Z = np.zeros((8,8))
# vector[x,y]
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)
