
class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        max_step = 0
        step = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                step += 1
            
            else:
                step = 0
            
            max_step = max(step, max_step)
            
        return max_step
        