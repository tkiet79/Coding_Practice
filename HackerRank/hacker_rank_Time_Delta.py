import datetime
n = int(input())
format_str = 'Day dd Mon yyyy hh:mm:ss +xxxx'
for _ in range(n):
    t1 = datetime.strptime(format_str)
    t2 = datetime.strptime(format_str)

print(t1)
print(t2)