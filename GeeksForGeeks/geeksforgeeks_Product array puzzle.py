#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        
        if n == 1: 
            return [1]
            
        # Mảng kết quả khởi tạo toàn 1
        res = [1] * n
        
        # Bước 1: Tính tích dồn từ TRÁI sang
        # res[i] sẽ chứa tích của các số từ arr[0] đến arr[i-1]
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= arr[i]
            
        # Bước 2: Tính tích dồn từ PHẢI sang và nhân vào kết quả
        # right_product sẽ chứa tích của các số từ arr[i+1] đến cuối
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= arr[i]
            
        return res

        