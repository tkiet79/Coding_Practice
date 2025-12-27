class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_MAP = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Lặp qua chuỗi từ trái sang phải
        for i in range(n):
            current_value = ROMAN_MAP[s[i]]
            
            # Kiểm tra quy tắc trừ: Nếu ký tự hiện tại có giá trị nhỏ hơn
            # ký tự tiếp theo, thì ta trừ đi giá trị hiện tại.
            # Ví dụ: IV (I=1, V=5) -> 1 < 5, nên trừ 1.
            if i < n - 1 and current_value < ROMAN_MAP[s[i+1]]:
                total -= current_value
            else:
                # Ngược lại, cộng vào tổng
                total += current_value
                
        return total

        