#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        plus = []
        minus = []
        res = 1
        for value in arr:
            res*= value
            
            if value < 0:
                minus.append(value)
            elif value > 0:
                plus.append(value)
        
        if len(arr) == 3:
            return res
        plus.sort()
        minus.sort()
        if not plus:
            return minus[-1] * minus[-2] * minus[-3]
        
        elif not minus:
            return plus[-1] * plus[-2] * plus[-3]
        
        else:
            if len(plus) < 3:
                return minus[0] * minus[1] * plus[-1]
                
            plus_value = plus[-1] * plus[-2] * plus[-3]
            if len(minus) < 2:
                return plus_value
                
            compile_value = minus[0] * minus[1] * plus[-1]
            return max(plus_value, compile_value)
        
                
        