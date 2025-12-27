#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        check = dict.fromkeys(arr, 0)
        for value in arr:
            check[value] += 1
        
        times = sorted([i for i in check.values()])
        
        for key, value in check.items():
            if value == times[-2]:
                return key