class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        arr.sort()

        check = dict.fromkeys(arr, 0)
        for value in arr:
            check[value] += 1

        res = []
        max_count = 0
        for count in check.values():
            if count > max_count:
                max_count = count
        
        for candidate, count in check.items():
            if count == max_count:
               return candidate, max_count



        
        
    
