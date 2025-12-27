import numpy as np
N = input().split()
row = int(N[0])
cols = int(N[1])
print(np.eye(row, cols))