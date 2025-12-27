class Solution:
    def trailingZeroes(self, n):
        count = 0
        # Chia liên tục cho 5 để đếm số lượng thừa số 5
        while n >= 5:
            n //= 5  # Chia lấy phần nguyên
            count += n
            
        return count