s = "geEksforGEeks"  # geEksforG
stack = []
res = []
for value in s:
    stack.append(value)
    print(stack)
        
for val in stack:
    x = stack.pop()
    res.append(x)
    print(res)
        
print(''.join(res))
