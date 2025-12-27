import math

class Solution:
    def isPerfect(self, n):
        # Số 1 không phải số hoàn hảo (tổng ước thực sự là 0 != 1)
        if n <= 1: return False
        
        total = 1  # Luôn có ước là 1
        
        # Chỉ chạy đến căn bậc 2 của n
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                total += i
                
                # Nếu i không phải là căn bậc 2 chính xác (ví dụ 6*6=36), 
                # thì cộng thêm ước đối diện (n/i)
                if i != n // i:
                    total += n // i
                    
        # Kiểm tra tổng sau khi đã tìm HẾT các ước
        return total == n