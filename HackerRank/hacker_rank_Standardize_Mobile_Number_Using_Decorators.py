def wrapper(f):
    def fun(l):
        my_list = []
        for value in list(set(sorted((l)))):
            if len(value) == 10:
                my_list.append(value)
                
            elif len(value) == 11:
                my_list.append(value[1:])
                
            elif len(value) ==12:
                my_list.append(value[2:])
            elif len(value) ==13:
                my_list.append(value[3:])

        for val in sorted(my_list):  
            print('+91',' ',val[:5],' ',val[5:],sep='')
            
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
