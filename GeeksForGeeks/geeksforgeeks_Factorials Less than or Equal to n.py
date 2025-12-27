#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        res = []
        fact = 1
        i = 1
        
        # Chỉ chạy khi giai thừa hiện tại vẫn nhỏ hơn hoặc bằng n
        while fact <= n:
            res.append(fact)
            i += 1       # Tăng số nhân lên
            fact *= i    # Tính giai thừa tiếp theo
            
        return res
        
    	     