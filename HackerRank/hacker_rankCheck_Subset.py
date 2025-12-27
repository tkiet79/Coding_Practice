T = int(input())


for _ in range(T):
    is_subset = True
    num_of_element_set_A = int(input())
    element_set_A = (list(map(int,input().split())))
    num_of_element_set_B = int(input())
    element_set_B = (list(map(int,input().split())))

    for value in element_set_A:
        if value not in element_set_B:
            is_subset = False
    
    if is_subset == True:
        print("True")
    else:
        print("False")
        
   


