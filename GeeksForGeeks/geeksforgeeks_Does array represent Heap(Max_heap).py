class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n//2):
            l=2*i+1
            r=2*i+2
            if (l<n and arr[l]>arr[i]) or (r<n and arr[r]>arr[i]):
                return False
        return True