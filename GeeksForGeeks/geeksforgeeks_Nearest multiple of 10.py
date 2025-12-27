class Solution:
    def roundToNearest(self, s):
        # Chuyển thành list ký tự để dễ thay đổi (string trong Python là immutable)
        chars = list(s)
        n = len(chars)
        
        # Lấy chữ số cuối cùng
        last_digit = int(chars[-1])
        
        # TRƯỜNG HỢP 1: Làm tròn xuống (0-5)
        # Ví dụ: 125 -> 120
        if last_digit <= 5:
            chars[-1] = '0'
            return "".join(chars)
            
        # TRƯỜNG HỢP 2: Làm tròn lên (6-9)
        # Ví dụ: 128 -> 130
        else:
            chars[-1] = '0'
            i = n - 2 # Bắt đầu xét từ số áp chót
            
            # Vòng lặp để xử lý phép "nhớ 1"
            while i >= 0:
                if chars[i] == '9':
                    chars[i] = '0' # 9 nhớ 1 thành 0, tiếp tục nhớ sang trái
                    i -= 1
                else:
                    # Nếu không phải 9, cộng 1 và dừng lại
                    chars[i] = str(int(chars[i]) + 1)
                    return "".join(chars)
            
            # Nếu chạy hết vòng lặp mà vẫn còn nhớ (ví dụ 99 -> 00)
            # Ta cần thêm số 1 vào đầu (thành 100)
            return '1' + "".join(chars)