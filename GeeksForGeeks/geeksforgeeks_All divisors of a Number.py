import math

class Solution:
    def print_divisors(self, n):
        divisors = [] # Tạo một list để chứa các ước
        
        # Chạy i từ 1 đến căn bậc 2 của n
        # Phải cộng thêm 1 để vòng lặp chạm được tới mốc căn bậc 2
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i) # Thêm ước nhỏ (ví dụ 2)
                
                # Kiểm tra để tránh thêm trùng nếu là số chính phương (ví dụ 6x6=36)
                if i != n // i:
                    divisors.append(n // i) # Thêm ước lớn tương ứng (ví dụ 10)
        
        # Đề bài yêu cầu in tăng dần -> Phải sắp xếp lại
        divisors.sort()
        
        # In ra kết quả
        for d in divisors:
            print(d, end=" ")