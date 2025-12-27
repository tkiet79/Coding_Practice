#User function Template for python3
from collections import Counter
class Solution:
    def allPairs(self, target, arr1, arr2):
        counter = Counter(arr1)
        res = []
        for value in arr2:
            curr = target - value
            if curr in counter:
                res += [[curr, value]] * counter[curr]
   
        return sorted(res)
            
        
    
