class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        check = dict.fromkeys(arr, 0)
        for value in arr:
            check[value] += 1
        
        res = 0
        for num, count in check.items():
            if count > len(arr) // k:
                res += 1
        
        return res