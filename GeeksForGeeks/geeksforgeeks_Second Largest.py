class Solution:
    def getSecondLargest(self, arr):
        new_arr = list((sorted(set(arr))))
        return new_arr[-2]