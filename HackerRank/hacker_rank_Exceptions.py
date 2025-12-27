number_of_case = int(input())
my_list = []
error_list = []
for i in range(number_of_case):
    x = input().split()
    my_list.append(x)
    


for value in my_list:
    a = value[0]
    b = value[1]
    try:
        result = int(a) / int(b)
        print(int(result))
    except  ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except  ValueError as error:
        print("Error Code:",error)



