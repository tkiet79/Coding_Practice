n = int(input())
for _ in range(n):
    try:
        num = float(input())
        if num == 0:
            print('False')
        else:
            print('True')
    except ValueError:
        print('False')