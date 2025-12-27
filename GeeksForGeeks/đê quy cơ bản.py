# Bài 1: Tính tổng dãy số tự nhiên
def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n-1)

# Tính giai thừa
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# Bài 3: Tìm số Fibonacci
def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

# Bài 4: Đếm số chữ số
def count_num(n):
    if n < 10:
        return 1
    return 1 + count_num(n//10)

# Bài 5a: In mảng xuôi 
def print_strs(arr):
    if not arr: 
        return
    print(arr[0])
    print_strs(arr[1:])

# Bài 5b: In mảng xuôi 
def reverse(arr):
    if not arr: 
        return
    reverse(arr[1:])
    print(arr[0])

n = [10,20,30]
print(print_strs(n))