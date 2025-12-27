class Solution:
    def findElement(self, arr):
        n = len(arr)
        # Nếu mảng quá ngắn, không thể có số ở giữa thỏa mãn
        if n < 3: return -1
        
        # --- BƯỚC CHUẨN BỊ  ---
        # Tạo sẵn bảng tra cứu "số nhỏ nhất bên phải"
        # right_min[i] sẽ lưu số nhỏ nhất từ vị trí i đến cuối mảng
        right_min = [0] * n
        right_min[n-1] = arr[n-1]
        
        # Đi ngược từ cuối về đầu để điền bảng
        for i in range(n-2, -1, -1):
            right_min[i] = min(arr[i], right_min[i+1])
            
       
        
        
        left_max = arr[0] 
        
        for i in range(1, n-1):
           
            
            # LOGIC MỚI (Nhanh gấp n lần):
            # 1. arr[i] > left_max  --> Tương đương lớn hơn tất cả bên trái
            # 2. arr[i] < right_min[i+1] --> Tương đương nhỏ hơn tất cả bên phải
            
            if arr[i] > left_max and arr[i] < right_min[i+1]:
                return arr[i]
            
            # Cập nhật left_max trước khi qua vòng lặp mới
            # (Giống như việc nạp thêm phần tử vào danh sách 'left' ảo)
            if arr[i] > left_max:
                left_max = arr[i]
                
        return -1