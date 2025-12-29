class Solution:
    def findSum(self, s):
        total = 0
        n = len(s)
        sub_num = ''
    
        for value in s:
            if value.isdigit():
                sub_num += value
                
            elif not value.isdigit() and sub_num is not '':
                total += int(sub_num)
                sub_num = ''
        
        if len(sub_num) != 0:
            total += int(sub_num)
            
        return total
