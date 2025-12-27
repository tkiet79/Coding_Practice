T = int(input())
for _ in range(T):
    size = int(input())
    block = list(map(int,input().split()))
    i = 0
    k = size - 1
    my_list = []
    while i <= k:
        if block[i] <= block[k]:
            current = block[k]
            my_list.append(int(block[k]))
            k -= 1
        elif block[i] > block[k]:
            current = block[i]
            my_list.append(int(block[i]))
            i += 1
        
    if my_list != sorted(my_list)[::-1]:
        print('No')
    else:
        print('Yes')
        





