import numpy as np

def Normalization(vector_x):
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    res = (X - X_min) / (X_max - X_min)
    return res
    

X = np.random.randint(0, 100, size=(100, 5))
res = Normalization(X)
print(res)