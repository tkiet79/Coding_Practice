import re
N = int(input())
regex_pattern = r"^[7-9]{1}[0-9]{9}$"
for _ in range(N):
    phone_number = input()
    check =str(bool(re.match(regex_pattern, phone_number)))
    if check == 'True':
        print('YES')
    else:
        print('NO')
    