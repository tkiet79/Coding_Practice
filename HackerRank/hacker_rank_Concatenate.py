import numpy as np 
N,M,P = input().split()
arr_N = []
arr_M = []
for _ in range(int(N)):
    element_array_N = list(map(int,input().split()))
    arr_N.append(element_array_N)
for _ in range(int(M)):
    element_array_M = list(map(int,input().split()))
    arr_M.append(element_array_M)

result_arr = np.concatenate((np.array(arr_N),np.array(arr_M))).reshape(int(N)+int(M),int(P))

print(result_arr)



