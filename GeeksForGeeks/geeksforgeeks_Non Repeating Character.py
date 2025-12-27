class Solution:
    def nonRepeatingChar(self,s):
        arr = [i for i in s]
        check = dict.fromkeys(arr,0)
        
        for value in arr:
            check[value] += 1
        
        for num,count in check.items():
            if count == 1:
                return num
        return '$'
    
    