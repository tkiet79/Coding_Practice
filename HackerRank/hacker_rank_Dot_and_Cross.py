import numpy as np
num = int(input())
arr_A = []
arr_B = []
for _ in range(num):
    arr_A.append(list(map(int,input().split())))   
arr_A = np.array(arr_A)

for _ in range(num):
    arr_B.append(list(map(int,input().split())))   
arr_B =  np.array(arr_B)

print(np.dot(arr_A,arr_B))

