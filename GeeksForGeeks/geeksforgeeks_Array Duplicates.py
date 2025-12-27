class Solution:
    def findDuplicates(self, arr):
        check_dup = dict.fromkeys(arr,0)
        
        for value in arr:
            check_dup[value] += 1
            
        res = []
        for num,count in check_dup.items():
            if count == 2:
                res.append(num)
        
        return res
            
            
    