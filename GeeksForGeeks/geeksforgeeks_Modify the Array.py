#User function Template for python3
class Solution:
    def modifyAndRearrangeArr (self, arr):
        idx = 1
        while idx < len(arr):
            if arr[idx] == arr[idx-1]:
                arr[idx-1] = arr[idx-1] * 2
                arr[idx] = 0
                idx += 2
            else:
                idx += 1
                continue
        
        res = [val for val in arr if val != 0] + [val for val in arr if val == 0]
        return res
            
        
            
         
