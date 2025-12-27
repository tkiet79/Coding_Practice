class Solution:
    def primeFac(self, n):
        res = []
        
        # 1. Xử lý số 2 riêng (số nguyên tố chẵn duy nhất)
        if n % 2 == 0:
            res.append(2)
            while n % 2 == 0:
                n //= 2
        
        # 2. Xử lý các số lẻ từ 3 đến căn bậc 2 của n
        # Chỉ cần chạy đến sqrt(n) là đủ
        i = 3
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                # Chia n cho i đến khi không chia hết nữa
                # để đảm bảo tính "Unique" và giảm n xuống
                while n % i == 0:
                    n //= i
            i += 2  # Nhảy bước 2 để chỉ kiểm tra số lẻ (3, 5, 7...)
            
        # 3. Nếu sau khi chia hết mà n vẫn > 1 
        # thì n còn lại chính là số nguyên tố lớn nhất
        if n > 1:
            res.append(n)
            
        return res