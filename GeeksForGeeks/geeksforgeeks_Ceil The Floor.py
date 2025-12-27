class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # 1. LOGIC QUAN TRỌNG CẦN THÊM
        # Nếu x đã nằm trong mảng, thì Floor = x và Ceil = x.
        # Trả về luôn, không cần sort hay append làm gì cho rối.
        if x in arr:
            return [x, x]

        # 2. Nếu x chưa có, ta dùng đúng logic của bạn:
        # "Nhét" x vào để xem nó đứng thứ mấy
        arr.append(x)
        arr.sort()
        
        idx_x = arr.index(x)
        
        # Khởi tạo giá trị mặc định
        floor = -1
        ceil = -1
        
        # 3. Xử lý Floor (Nhìn sang trái)
        # Nếu x không đứng đầu, thì số bên trái (idx - 1) chính là Floor
        if idx_x > 0:
            floor = arr[idx_x - 1]
            
        # 4. Xử lý Ceil (Nhìn sang phải)
        # Nếu x không đứng cuối, thì số bên phải (idx + 1) chính là Ceil
        if idx_x < len(arr) - 1:
            ceil = arr[idx_x + 1]
            
        return [floor, ceil]
    
#----------------------------------------------------------------#
# cách 2: 
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # Khởi tạo giá trị mặc định là -1
        floor_val = -1
        ceil_val = float('inf') # Dùng vô cực để dễ tìm min
        
        for num in arr:
            # Tìm Floor: Số lớn nhất mà <= x
            if num <= x:
                floor_val = max(floor_val, num)
            
            # Tìm Ceil: Số nhỏ nhất mà >= x
            if num >= x:
                ceil_val = min(ceil_val, num)
                
        # Nếu ceil vẫn là vô cực nghĩa là không tìm thấy số nào >= x
        if ceil_val == float('inf'):
            ceil_val = -1
            
        return [floor_val, ceil_val]