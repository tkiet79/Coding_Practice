import re

# Đọc số lượng dòng N
N = int(input())

# Khởi tạo một chuỗi rỗng để chứa TOÀN BỘ code CSS
css_code = ""

# Đọc N dòng tiếp theo và ghép chúng lại thành MỘT chuỗi lớn
# (Việc này dễ xử lý hơn là đọc từng dòng)
for _ in range(N):
    css_code += input() + "\n"  # Thêm ký tự xuống dòng để giữ nguyên cấu trúc

# --- Bắt đầu phần Regex ---

# 1. ĐỊNH NGHĨA MẪU REGEX THỨ NHẤT: Tìm các khối { ... }
#
#    \{     -> Khớp với ký tự { (dấu \ dùng để "escape" nó)
#    ([^}]*) -> Đây là MẪU CHÍNH:
#               ( )   -> Bắt giữ (capture group) mọi thứ bên trong.
#               [^}]  -> Khớp với BẤT KỲ ký tự nào KHÔNG PHẢI là }
#               * -> Khớp 0 hoặc nhiều lần các ký tự ở trên.
#    \}     -> Khớp với ký tự }
#
# => Mẫu này sẽ tìm và "bắt" (trả về) tất cả text ở giữa { và }
block_pattern = r"\{([^}]*)\}"


# 2. ĐỊNH NGHĨA MẪU REGEX THỨ HAI: Tìm mã màu Hex
#
#    #         -> Ký tự thăng
#    (?:...)   -> Một "non-capturing group" (chỉ để nhóm lại, không "bắt")
#    [a-f0-9]{6} -> Khớp 6 ký tự, là 'a' đến 'f' hoặc '0' đến '9'
#    |         -> Toán tử HOẶC (OR)
#    [a-f0-9]{3} -> Khớp 3 ký tự, là 'a' đến 'f' hoặc '0' đến '9'
#    \b        -> Ranh giới từ (word boundary). 
#                 Đảm bảo nó không khớp #1234567 (quá dài)
#
# => Mẫu này tìm # theo sau là 3 HOẶC 6 ký tự hex
hex_pattern = r"#(?:[a-f0-9]{6}|[a-f0-9]{3})\b"


# 3. THỰC THI BƯỚC 1:
#    Tìm tất cả các 'khối' trong toàn bộ code CSS.
#    Kết quả là một LIST các chuỗi text bên trong { }.
#    Ví dụ: ['\n    color: #Fffdf8; ...', '\n    background-color: #ABC; ...']
all_blocks = re.findall(block_pattern, css_code)


# 4. LẶP QUA TỪNG KHỐI ĐÃ TÌM ĐƯỢC
for block in all_blocks:
    
    # 5. THỰC THI BƯỚC 2:
    #    Tìm tất cả các mã hex (theo mẫu hex_pattern) 
    #    CHỈ bên trong chuỗi 'block' này.
    #    re.IGNORECASE -> Cờ để khớp cả chữ hoa (A-F)
    #
    #    Kết quả là một LIST các mã màu tìm được, 
    #    ví dụ: ['#Fffdf8', '#aef', '#f9f9f9', '#fff']
    hex_codes = re.findall(hex_pattern, block, re.IGNORECASE)
    
    # 6. IN KẾT QUẢ:
    #    Lặp qua list mã màu vừa tìm được và in ra từng cái
    for code in hex_codes:
        print(code)

#Lọc lần 1: re.findall(block_pattern, ...) chỉ lấy text bên trong {}. Điều này ngay lập tức giải quyết vấn đề lớn nhất: nó tự động bỏ qua #BED và #Cab vì chúng nằm bên ngoài dấu {}.

#Lọc lần 2: re.findall(hex_pattern, ...) sau đó mới tìm các mã màu hợp lệ bên trong các đoạn text đã được lọc đó.