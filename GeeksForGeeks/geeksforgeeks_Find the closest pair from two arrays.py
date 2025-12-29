#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        dif = float('inf')
        N = 0
        M = m-1
        
        
        while N < n and M >= 0:
            curr_sum = arr[N] + brr[M]
            
            if abs(curr_sum - x) < dif:
                dif = abs(curr_sum - x)
                res = [arr[N], brr[M]]
                
            
            if curr_sum < x:
                N += 1
            elif curr_sum > x:
                M -= 1
            else:
                return res
        
        return res
        