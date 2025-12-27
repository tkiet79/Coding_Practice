s = 'aabb'
res = [s[0]]
for value in s:
    if value != res[-1]:
        res.append(value)

print(''.join(res))

