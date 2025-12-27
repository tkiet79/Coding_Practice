#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        arr1.sort()
        arr2.sort(reverse=True)
        res = 0
        for i in range(len(arr1)):
            res += arr1[i] * arr2[i]
        
        return res