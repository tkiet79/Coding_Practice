import numpy as np
num = input().split()
arr = []
for _ in range(int(num[0])):
    arr.append(list(map(float,input().split())))
arr = np.array(arr)

print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr))
