class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        largest = arr[-1] - k
        smallest = arr[0] + k
        ans = arr[-1] - arr[0]
        
        for i in range(n-1):
            if arr[i+1] - k < 0:
                continue
            
            curr_max = max(largest, arr[i] + k)
            curr_min = min(smallest, arr[i+1] - k)
            ans = min(ans, curr_max - curr_min)
        return ans
