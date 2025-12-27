import itertools
def function(x):
    return x**2
all_list = []
K,M = input().split()
for _ in range(int(K)):
    value_input = list(map(int, input().split()))
    element = value_input[1:]
    value = [function(x) % int(M) for x in element]
    all_list.append(value)
all_combinations = itertools.product(*all_list)

max_value = 0
for combo in all_combinations:
    curr_sum = sum(combo)
    current_S = curr_sum % int(M)
    if current_S >= max_value:
        max_value=current_S

print(max_value) 

                

