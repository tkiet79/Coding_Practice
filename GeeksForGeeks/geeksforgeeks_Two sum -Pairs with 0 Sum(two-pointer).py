#User function Template for python3
class Solution:
    def getPairs(self, arr):
        arr.sort()
        
        
        left = 0
        right = len(arr) - 1
        result = []
        while left < right:
            if arr[left] + arr[right] < 0:
                left = left + 1
            elif arr[left] + arr[right] > 0:
                right = right - 1
            elif arr[left] + arr[right] == 0:
                result.append([arr[left],arr[right]])
                while left<right and arr[left+1]==arr[left]:
                    left=left+1
                while left<right and arr[right]==arr[right-1]:
                    right=right-1
                
                left = left + 1
                right = right - 1
        return result






