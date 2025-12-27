cube = lambda x: int(x**3)

def fibonacci(n):
    fib = []
    a, b =0, 1
    for _ in range(n):
        fib.append(a)
        temp = a
        a = b
        b = temp + b
    return fib

        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))