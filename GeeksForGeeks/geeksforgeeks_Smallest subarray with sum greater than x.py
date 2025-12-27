class Solution:
    def smallestSubWithSum(self, x, arr):
        # sliding window
        left = 0
        total = 0
        right = 0
        min_len = float('inf')
        while right < len(arr) and left <= right:
            total += arr[right]
            right += 1
            while total > x:
                min_len = min(right - left , min_len)
                total -= arr[left]
                left += 1
                
        if min_len == float('inf') :
            return 0
        return min_len
    
            
    
        
        

        

        
        
        
        
        
         

            
        
             
        