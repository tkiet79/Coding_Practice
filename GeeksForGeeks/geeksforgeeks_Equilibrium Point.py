arr = [-7, 1, 5, 2, -4, 3, 0]
n = len(arr)
for i in range(1,n-1):
    if sum(arr[:i]) == sum(arr[i+1:n]):
        print(i)