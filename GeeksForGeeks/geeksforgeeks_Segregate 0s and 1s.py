#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        left = [i for i in arr if i == 0]
        right = [i for i in arr if i == 1]
        arr[:] = left + right
        return arr