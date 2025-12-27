element_of_set_A = set(map(int,input().split()))
n = int(input())
is_strict_superset = []
for _ in range(n):
    element_of_other_set = set(map(int,input().split()))
    if element_of_other_set.issubset(element_of_set_A):
        is_strict_superset.append('True')
    else:
        is_strict_superset.append('False')
if 'False' in is_strict_superset:
    print("False")
else:
    print("True")

    

