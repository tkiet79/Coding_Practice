class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True