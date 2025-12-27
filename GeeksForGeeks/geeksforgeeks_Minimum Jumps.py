class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Trường hợp 1: Mảng chỉ có 1 phần tử hoặc ít hơn -> Đã ở đích
        if n <= 1:
            return 0
            
        # Trường hợp 2: Không thể nhảy đi đâu từ bước đầu tiên
        if arr[0] == 0:
            return -1

        # Khởi tạo
        maxReach = arr[0]  # Vị trí xa nhất có thể vươn tới
        steps = arr[0]     # Số bước còn lại của lần nhảy hiện tại
        jumps = 1          # Đã nhảy 1 phát từ arr[0]
        
        # Duyệt từ phần tử thứ 2 (index 1) đến hết mảng
        for i in range(1, n):
            # Nếu đã đến đích (phần tử cuối cùng)
            if i == n - 1:
                return jumps
            
            # Cập nhật tầm với xa nhất
            maxReach = max(maxReach, i + arr[i])
            
            # Tiêu tốn 1 bước để đi đến i
            steps -= 1
            
            # Nếu hết bước của lần nhảy hiện tại
            if steps == 0:
                jumps += 1  # Bắt buộc phải nhảy thêm 1 phát nữa
                
                # Kiểm tra xem có bị mắc kẹt không?
                # Nếu vị trí hiện tại (i) đã >= tầm với xa nhất (maxReach)
                # nghĩa là không thể tiến xa hơn được nữa.
                if i >= maxReach:
                    return -1
                
                # Nạp lại số bước cho lần nhảy mới
                # Số bước mới = (Đích xa nhất có thể tới) - (Vị trí hiện tại)
                steps = maxReach - i
                
        return -1