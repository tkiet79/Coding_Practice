#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        arr = [char for char in string if char != ' ']
        n = len(arr)
        if n < 26:
            return False
        
        check = []
        for value in arr:
            check.append(value)
        
        check = len(list(set(arr)))
        
        return check + k >= 26
        
        
            
         
             
        
        
        