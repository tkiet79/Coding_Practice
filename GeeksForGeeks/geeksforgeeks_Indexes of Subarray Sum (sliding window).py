#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        left = 0
        n = len(arr)
        current_sum = 0
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left < right:
                current_sum -= arr[left]
                left +=1
            
            if current_sum == target:
                return [left + 1, right + 1]
        else:
            return [-1]
        




    
    




        

    
                



