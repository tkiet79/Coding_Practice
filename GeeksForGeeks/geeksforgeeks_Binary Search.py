class Solution:
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr) - 1
    
        while left <= right:
            mid = (left + right) // 2  # Lấy điểm giữa
        
            if arr[mid] == k:
                return mid  # Tìm thấy, trả về vị trí
            
            elif arr[mid] < k:
                left = mid + 1  # Tìm tiếp ở bên phải
            
            else:
                right = mid - 1 # Tìm tiếp ở bên trái
            
        return -1  # Không tìm thấy


        