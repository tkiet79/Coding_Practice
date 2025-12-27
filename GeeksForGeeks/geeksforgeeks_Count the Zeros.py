#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        count = 0
        for i in range(-1, -len(arr) -1 , -1):
            if arr[i] == 0:
                count += 1
            elif arr[i] == 1:
                break
        return count