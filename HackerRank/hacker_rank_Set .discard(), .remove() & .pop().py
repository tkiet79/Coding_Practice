n = int(input())
s = set(map(int, input().split()))
the_number_of_commands = int(input())
for _ in range(the_number_of_commands):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
print(sum(s))
