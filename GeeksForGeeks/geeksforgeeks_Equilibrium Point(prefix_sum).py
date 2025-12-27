# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        left[0] = arr[0]
        right[n-1] = arr[n-1]
        
        for i in range(1,n):
            left[i] = left[i-1] + arr[i]
        
        for j in range(n-2,-1,-1):
            right[j] = right[j+1] + arr[j]
        
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1