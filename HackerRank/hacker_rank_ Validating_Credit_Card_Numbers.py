import re
n = int(input())
Regex_partern = r"^(([4-6])([0-9]{3})([-][0-9]{4}){3}|[0-9]{15})$"
for i in range(n):
    credit_card_numbers = input()
    check = str(bool(re.match(Regex_partern, credit_card_numbers)))
    if check == 'True':
        print('Valid')
    else:
        print('Invalid')

