#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        check = dict.fromkeys(arr,0)
        for value in arr:
            check[value] += 1
            
        
        for num, count in check.items():
            if count == 1:
                return num
        return 0
                
