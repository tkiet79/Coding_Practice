m = input().split()
the_elements_of_the_array = input().split()
A = set(input().split())
B = set(input().split())



happiness = 0
for value in the_elements_of_the_array:
    if value in A:
        happiness += 1
    elif value in B:
        happiness -= 1
print(happiness)

