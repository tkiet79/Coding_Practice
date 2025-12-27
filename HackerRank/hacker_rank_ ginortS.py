s = input()
lower_list = []
upper_list = []
odd_num = []
even_num = []

for char in s:

    if char.isdigit():
        if int(char) % 2 != 0:
            odd_num.append(char)
        elif int(char) % 2 == 0:
            even_num.append(char)
    elif char == char.upper():
        upper_list.append(char)
    elif char == char.lower():
        lower_list.append(char)

lower_list.sort()
upper_list.sort()
odd_num.sort()
even_num.sort()
        

print(*lower_list,*upper_list,*odd_num,*even_num,sep='')



