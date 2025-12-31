#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        
        idx = 1
        if len(arr) < 2:
            return arr
        
        res = []
        for value in arr:
            if not res:
                res.append(value)
            
            elif (res[-1] < 0 and value >= 0) or (res[-1] >= 0 and value < 0):
                res.pop()
            
            else:
                res.append(value)
                
        return res
                
                