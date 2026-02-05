import numpy as np

arr = np.random.randint(1, 101, size= (5,5))
sum_per_row = np.linalg.norm(arr, axis=1, keepdims=True)
res = arr / sum_per_row
print(res)

