class Solution:
    def filterByDigits(self, arr):
        str_arr = list(map(str, arr))
        res = []
        my_lst = ['1', '2', '3']
        
        for value in str_arr:
            curr_str = [char for char in value if char in my_lst]
            if len(curr_str) == len(value):
                res.append(value)
                
                
        if not res:
            return[-1]
        return res
