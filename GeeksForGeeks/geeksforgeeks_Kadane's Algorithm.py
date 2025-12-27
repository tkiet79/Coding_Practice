class Solution:
    def maxSubarraySum(self, arr):
        max_subarray = max(arr)
        if max_subarray < 0:
            return max_subarray
            
        current_sum = 0
        left = 0
        n = len(arr)
        
        if n == 1:
            return arr[0]

        for right in range(left, n):
            current_sum += arr[right]
            if current_sum < 0:
                current_sum = 0
                left = right + 1

            if current_sum > max_subarray:
                max_subarray = current_sum

        return max_subarray
    

   




