import numpy as np
num = input().split()
arr = []
for _ in range(int(num[0])):
    arr.append(list(map(float,input().split())))
arr = np.array(arr)
print(int(np.max(np.min(arr, axis = 1))))
