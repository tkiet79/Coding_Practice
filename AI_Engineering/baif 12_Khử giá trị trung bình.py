import numpy as np

arr = np.random.randint(1, 101, size = (10,10))
row_mean = np.mean(arr, axis=1, keepdims=True)
X_centered = arr - row_mean
print(X_centered)