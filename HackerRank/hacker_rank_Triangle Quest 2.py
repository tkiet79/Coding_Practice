n =int(input())+1
my_list = "".join(map(str,[x for x in range(0,n)]))

for i in range(n-1):
    left_part = my_list[1:i+2]
    right_part = my_list[i:0:-1]
    print(int(left_part+right_part))

    
