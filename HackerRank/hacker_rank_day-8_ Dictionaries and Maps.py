n = int(input())
phone_book = {}
for i in range(n):
    information_input = input().split()
    phone_book.update({information_input[0]: information_input[1]})

query_names_list =[]
while True:
    try:
        query_names = input()
        query_names_list.append(query_names)

        if query_names in phone_book:
            print(f"{query_names}={phone_book[query_names]}")
        else:
            print("Not found")
    except EOFError:
        break