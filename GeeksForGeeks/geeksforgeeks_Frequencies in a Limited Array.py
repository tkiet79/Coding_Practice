class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        # Bước 1: Tạo Hash Map để đếm
        # (Bạn có thể dùng thư viện collections.Counter cho nhanh, nhưng code tay cho dễ hiểu)
        count_map = {}
        
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Bước 2: Sửa trực tiếp vào mảng arr (In-place) theo yêu cầu đề bài
        # Duyệt từ index 0 đến n-1
        for i in range(n):
            target_number = i + 1  # Index 0 thì tìm số 1, Index 1 tìm số 2...
            
            if target_number in count_map:
                arr[i] = count_map[target_number]
            else:
                arr[i] = 0 # Nếu số đó không xuất hiện thì ghi 0
                
        # Lưu ý: Hàm này thường không yêu cầu return, mà sửa trực tiếp arr.
        # Nhưng nếu cần in ra để test thì:
        return arr
        
        

