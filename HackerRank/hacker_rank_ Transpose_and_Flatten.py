import numpy
N, M =map(int,input().split())
arr = []
for i in range(N):
    element = list(map(int,input().split()))
    arr.append(element)
arrs = numpy.array(arr)
print(numpy.transpose(arrs))
print(numpy.array(arr).flatten())

        
