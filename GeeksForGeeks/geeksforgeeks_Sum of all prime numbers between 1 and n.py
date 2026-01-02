#User function Template for python3

class Solution:
    def is_prime(self, n):
        import math
        """Hàm kiểm tra số nguyên tố (chỉ cho n > 0)"""
        # 1 và 0 không phải là số nguyên tố
        if n <= 1:
            return False
        # 2 là số nguyên tố
        if n == 2:
            return True
        # Bất kỳ số chẵn nào khác (ngoại trừ 2) đều không phải số nguyên tố
        if n % 2 == 0:
            return False
    
        # hàm range(start, stop, step) với start là chỉ số bắt đầu, stop là chỉ số dừng lại giá trị cuối cùng sẽ là end - 1, step là số khoảng cách giữa 2 giá trị
        # vì Bất kỳ số chẵn nào khác (ngoại trừ 2) đều không phải số nguyên tố nên ta chỉ xét các số lẻ
        # Nếu chúng ta không tìm thấy ước số nào từ 2 cho đến sqrt(n) (sqrt là căn bậc 2), thì n chắc chắn là số nguyên tố.
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    
    # Nếu không tìm thấy ước số nào, nó là số nguyên tố
        return True
    
         
	def prime_Sum(self, n):
	    res = 0
	    for i in range(2, n+1):
	        if self.is_prime(i):
	            res += i
	    
	    
	    return res
	    
	    
	            
	    
	    
		