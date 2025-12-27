class Solution:
    def pattern(self, n):
        result = []
        
        def recursive_helper(current_val):
            # 1. Thêm số vào lúc đi xuống (Trước khi gọi đệ quy)
            result.append(current_val)
            
            # 2. Điều kiện dừng và quay đầu
            if current_val <= 0:
                return # Chạm đáy thì dừng việc đi xuống
            
            # 3. Gọi đệ quy (Tiếp tục đi xuống)
            recursive_helper(current_val - 5)
            
            # 4. Thêm số vào lúc đi lên (Sau khi hàm đệ quy bên trên chạy xong)
            # Đây là phép thuật của đệ quy: Code chạy dòng này khi các hàm con đã kết thúc (Backtracking)
            result.append(current_val)

        recursive_helper(n)
        
        return result