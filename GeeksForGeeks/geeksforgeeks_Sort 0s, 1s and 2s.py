# Dutch National Flag Algorithm
class Solution:
    def sort012(self, arr):
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # Gặp số 0: Đổi chỗ về đầu (vùng low)
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # Gặp số 1: Để nguyên, đi tiếp
                mid += 1
            else:
                # Gặp số 2: Đổi chỗ về cuối (vùng high)
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr
        