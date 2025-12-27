class Solution:
    def countFreq(self, arr, target):
        check = dict.fromkeys(arr,0)
        
        for value in arr:
            check[value] += 1
        
        for num, count in check.items():
            if num == target:
                return count
        else:
            return 0