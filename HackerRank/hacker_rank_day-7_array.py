
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    for value in arr[::-1]:
        print(value ,end=" ") 
   


