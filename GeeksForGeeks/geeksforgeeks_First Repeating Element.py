class Solution:
    def firstRepeated(self,arr):
        check = dict.fromkeys(arr,0)
        for value in arr:
            check[value] += 1
        
        for num, count in check.items():
            
            if count >= 2:
                return arr.index(num) + 1
                
        return -1
                
        