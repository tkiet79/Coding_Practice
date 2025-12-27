import numpy as np
arr_A = np.array(list(map(int, input().split())))
arr_B = np.array(list(map(int, input().split())))
print(np.inner(arr_A,arr_B))
print(np.outer(arr_A,arr_B))