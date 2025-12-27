N = int(input())
my_list = []
for _ in range(N):
    user_input = input().strip()
    my_list.append(user_input)
my_set = set(my_list)
print(len(my_set))
print(my_set)