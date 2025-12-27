#User function Template for python3

class Solution:
    def findIndex (self,arr, key ):
        n = len(arr) 
        res = []
        if key not in arr:
            return [-1, -1]
            
        for i in range(n):
            if arr[i] == key:
                res.append(i)
                break
            
        
        for i in range(n-1 ,-1 ,-1):
            if arr[i] == key:
                res.append(i)
                break
        
        
        
    
        return res