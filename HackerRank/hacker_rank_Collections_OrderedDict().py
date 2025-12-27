from collections import OrderedDict
n = int(input())
Net_Price = OrderedDict()
for _ in range(n):
    cmd = input().split()
    name = ' '.join(cmd[:-1])
    Net_Price[name] = Net_Price.get(name, 0) + int(cmd[-1])


for value in Net_Price.items():
    print(*value)