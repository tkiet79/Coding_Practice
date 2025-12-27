class Solution:
    def missingNum(self, arr):
        n = len(arr) + 2
        new_arr = [i for i in range(1, n)]
        return sum(new_arr) - sum(arr)

    


    
     

    
