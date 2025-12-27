class Solution:
    def firstElementKTime(self, arr,k):
        check = dict.fromkeys(arr,0)
        for value in arr:
            check[value] += 1
            if check[value] == k:
                return value
        return -1
        

        
        
    
