import numpy as np

arr = np.random.randint(1, 101, size=(10,10))
mean = np.mean(arr, axis=0, keepdims=True)
std = np.std(arr, axis=0, keepdims=True)

Z = (arr - mean) / std
print(Z)