import email.utils
import re
email_valid = r"^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z][a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
N = int(input())
for _ in range(N):
    email_address = email.utils.parseaddr(input())
    name, emails = email_address
    check =str(bool(re.match(email_valid, emails)))
    if check == 'True':
        print(email.utils.formataddr(email_address))
    else:
        continue