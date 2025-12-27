class Solution:
    def median(self, arr):
        import math
        arr.sort()
        n = len(arr)
        if n % 2 != 0:
            return arr[int(((n+1)/2)-1)]
        return math.floor((arr[int(n/2) - 1] + arr[int(n/2)]) / 2)
    
    def mean(self, arr):
        return int(sum(arr) / len(arr))