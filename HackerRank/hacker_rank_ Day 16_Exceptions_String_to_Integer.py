s = input()
try:
    s = int(s)
    print(s)
except ValueError:
    print('Bad String')