n = int(input())
element = set(map(int,input().split()))
number_of_other_list = int(input())

for i in range(number_of_other_list):
    cmd = input().split()
    update_list = set(map(int,input().split()))
    if cmd[0] == 'update':
       element.update(update_list)
    elif cmd[0] == 'intersection_update':
        element &= update_list
    elif cmd[0] == 'symmetric_difference_update':
        element ^= update_list
    elif cmd[0] == 'difference_update':
        element.difference_update(update_list)

print(sum(element))

