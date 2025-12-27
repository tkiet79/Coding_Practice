class Solution:
    def transitionPoint(self, arr): 
        for value in arr:
            if value == 1:
                return arr.index(value)
        return -1