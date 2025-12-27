x, k = map(int, input().split())

# 2. Đọc dòng thứ hai (chính là chuỗi đa thức)
polynomial_string = input()

# 3. Đây là "mẹo":
# Dùng hàm eval() để "thực thi" chuỗi đa thức.
# eval() sẽ tự động tìm biến 'x' mà chúng ta đã định nghĩa
# ở dòng 1 và thay thế nó vào phép tính.
# Ví dụ: eval("x**3 + 1", {'x': 1}) sẽ là 1**3 + 1 = 2
# (Trong trường hợp này, chúng ta không cần truyền dict {'x': 1}
# vì 'x' đã tồn tại trong phạm vi (scope) toàn cục)
result = eval(polynomial_string)

if result == k:
    print('True')
else:
    print('False')


    


