import numpy as np
n = input().split()
arr_A = []
arr_B = []
for i in range(int(n[0])):
    element_in_array_A = list(map(int,input().split()))
    arr_A.append(element_in_array_A)

for j in range(int(n[0])):
    element_in_array_B = list(map(int,input().split()))
    arr_B.append(element_in_array_B)

arr_A = np.array(arr_A)
arr_B = np.array(arr_B)

print(arr_A + arr_B)
print(arr_A - arr_B)
print(arr_A * arr_B)
print(arr_A // arr_B)
print(arr_A % arr_B)
print(arr_A ** arr_B)

