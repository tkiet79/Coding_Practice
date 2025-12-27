class Solution:
    def minAnd2ndMin(self, arr):
        arr = sorted(set(arr))
        if len(arr) < 2:
            return [-1]
        return [arr[0], arr[1]]
        
