#User function Template for python3

class Solution:
    def maxValue(self, arr):
        arr.sort()
        res = []
        for i in range(len(arr)):
            res.append(arr[i] * i)
        return sum(res) % (10**9 + 7)


        
        
      
