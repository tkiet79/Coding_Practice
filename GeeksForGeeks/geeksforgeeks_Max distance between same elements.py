class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        max_distance = 0
        check = {}
        for i in range(len(arr)):
            if arr[i] not in check.keys():
                check[arr[i]] = i
            
            else:
               max_distance = max(max_distance, i - check[arr[i]])  
        
        return max_distance