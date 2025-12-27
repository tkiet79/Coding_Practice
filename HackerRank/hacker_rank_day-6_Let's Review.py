n = int(input())
user_input = []
for i in range(n):
    s = input()
    user_input.append(s)
for value in user_input:
    even = [value[i] for i in range(len(value)) if i % 2 ==0]
    odd = [value[i] for i in range(len(value)) if i % 2 !=0]
    x = "".join(even)
    y = "".join(odd)    
    print(x,y,sep=" ")


