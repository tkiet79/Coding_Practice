#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        plus= []
        minus = []
        for val in arr:
            if val < 0:
                minus.append(val)
            else:
                plus.append(val)
        
        arr[:] = plus + minus
        
        

       
                