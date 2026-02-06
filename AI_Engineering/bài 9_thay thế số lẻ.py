import numpy as np

arr = np.random.randint(1, 101, size=10) 
print("mảng ban đầu:          ", arr)
arr[arr % 2 != 0] = -1
print("mảng sau khi thay đổi: ", arr)