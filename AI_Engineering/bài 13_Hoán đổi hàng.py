import numpy as np

arr = np.random.randint(1,101,size=(4,4))
print("mảng ban đầu:\n ", arr)
arr = arr[[3,1,2,0]]
print("\nmảng sau khi swap: \n", arr)