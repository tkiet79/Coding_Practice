
n = int(input())
a = input().strip().split()
N = int(input())
b = input().strip().split()
newlist = []


list_a = set(list(map(int, a)))
list_b = set(list(map(int, b)))

x = list_a.difference(list_b)
y = list_b.difference(list_a)

total_difference = x.union(y)
final_list = list(total_difference)
final_list.sort()
for value in final_list:
    print(value)

