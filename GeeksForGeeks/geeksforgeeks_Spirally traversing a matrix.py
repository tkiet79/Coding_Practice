class Solution:
    def spirallyTraverse(self, mat):
        result = []
    
    # Kiểm tra ma trận rỗng
        if not mat:
            return result
    
    # Khởi tạo các biên
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
    
        while top <= bottom and left <= right:
        # 1. Đi từ Trái -> Phải (trên hàng 'top')
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1 # Thu hẹp biên trên
        
        # 2. Đi từ Trên -> Dưới (trên cột 'right')
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1 # Thu hẹp biên phải
        
        # 3. Đi từ Phải -> Trái (trên hàng 'bottom')
            if top <= bottom: # Kiểm tra lại để tránh lặp nếu chỉ còn 1 hàng
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1 # Thu hẹp biên dưới
        
        # 4. Đi từ Dưới -> Trên (trên cột 'left')
            if left <= right: # Kiểm tra lại để tránh lặp nếu chỉ còn 1 cột
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1 # Thu hẹp biên trái
            
        return result


        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        