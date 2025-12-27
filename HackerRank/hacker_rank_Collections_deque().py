from collections import deque
n =int(input())
my_list = deque([])
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'append':
        my_list.append(int(cmd[1]))
    if cmd[0] == 'appendleft':
        my_list.appendleft(int(cmd[1]))
    if cmd[0] == 'pop':
        my_list.pop()
    if cmd[0] == 'popleft':
        my_list.popleft()
print(*my_list)

