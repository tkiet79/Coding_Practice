import re

UID_format = r"^(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})(?!.*(.).*\1)[a-zA-Z0-9]{10}$"
# --- GIẢI THÍCH BIỂU THỨC CHÍNH QUY (REGEX) ---
#
# Biểu thức đầy đủ:
# r"^(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})(?!.*(.).*\1)[a-zA-Z0-9]{10}$"
#
# --- GIẢI THÍCH TỔNG QUAN ---
#
# Biểu thức này dùng để xác thực một chuỗi (ví dụ: User ID) phải tuân theo một bộ quy tắc rất nghiêm ngặt:
# - Độ dài cố định (10 ký tự).
# - Chỉ chứa các ký tự cụ thể (chữ cái và số).
# - Phải có đủ số lượng chữ hoa và số.
# - Không được phép có bất kỳ ký tự nào lặp lại.
#
# Ký hiệu r"..." ở đầu là đặc trưng của ngôn ngữ Python, cho biết đây là một "chuỗi thô" (raw string).
# Điều này giúp Python không hiểu sai các ký tự như \ (dấu gạch chéo ngược).
#
# --- PHÂN TÍCH TỪNG THÀNH PHẦN ---
#
# 1. ^
#    - Ý nghĩa: Ký tự "neo" (anchor).
#    - Giải thích: Khẳng định rằng sự so khớp phải bắt đầu NGAY TẠI ĐẦU CHUỖI.
#
# 2. (?=(?:.*[A-Z]){2,})
#    - Ý nghĩa: "Positive Lookahead" (Kiểm tra phía trước - Khẳng định).
#    - Giải thích: Nó KIỂM TRA một điều kiện mà KHÔNG "TIÊU THỤ" bất kỳ ký tự nào.
#    - Chi tiết:
#        - (?=...): Cú pháp của Positive Lookahead.
#        - (?:...): Một "nhóm không bắt giữ" (non-capturing group). Nó nhóm các thành phần lại.
#        - .*: Khớp với bất kỳ ký tự nào (.) 0 hoặc nhiều lần (*).
#        - [A-Z]: Khớp với MỘT ký tự IN HOA (từ A đến Z).
#        - (?:.*[A-Z]): Nhóm này có nghĩa là "tìm bất kỳ chuỗi ký tự nào, theo sau là một chữ IN HOA".
#        - {2,}: Lượng từ (quantifier). Yêu cầu nhóm (?:.*[A-Z]) phải xuất hiện ÍT NHẤT 2 LẦN.
#    - Kết luận: Chuỗi phải chứa ÍT NHẤT 2 KÝ TỰ IN HOA.
#
# 3. (?=(?:.*[0-9]){3,})
#    - Ý nghĩa: Một "Positive Lookahead" thứ hai.
#    - Giải thích: Tương tự như phần 2, đây là một điều kiện bắt buộc khác.
#    - Chi tiết:
#        - (?:.*[0-9]): Một nhóm không bắt giữ, khớp với "bất kỳ chuỗi ký tự nào, theo sau là một SỐ (0-9)".
#        - {3,}: Lượng từ, yêu cầu nhóm này phải xuất hiện ÍT NHẤT 3 LẦN.
#    - Kết luận: Chuỗi phải chứa ÍT NHẤT 3 KÝ TỰ SỐ.
#
# 4. (?!.*(.).*\1)
#    - Ý nghĩa: "Negative Lookahead" (Kiểm tra phía trước - Phủ định).
#    - Giải thích: Nó khẳng định rằng mẫu bên trong KHÔNG ĐƯỢC PHÉP tồn tại trong chuỗi.
#    - Chi tiết:
#        - (?!...): Cú pháp của Negative Lookahead.
#        - (.): Một "nhóm bắt giữ" (capturing group 1). Nó khớp 1 KÝ TỰ BẤT KỲ và LƯU TRỮ ký tự đó.
#        - .*: Khớp với bất kỳ ký tự nào, 0 hoặc nhiều lần (các ký tự ở giữa).
#        - \1: Một "tham chiếu ngược" (backreference). Nó khớp với CHÍNH XÁC KÝ TỰ đã được lưu trữ trong nhóm 1.
#        - .*(.).*\1: Toàn bộ mẫu này tìm kiếm "bất kỳ ký tự nào, theo sau là một ký tự (nhóm 1), theo sau là bất kỳ ký tự nào, và sau đó là chính ký tự (nhóm 1) lặp lại".
#    - Kết luận: Chuỗi KHÔNG ĐƯỢC CHỨA BẤT KỲ KÝ TỰ NÀO LẶP LẠI.
#
# 5. [a-zA-Z0-9]{10}
#    - Ý nghĩa: Đây là phần "thân" chính của biểu thức, phần duy nhất thực sự "tiêu thụ" và so khớp các ký tự.
#    - Chi tiết:
#        - [a-zA-Z0-9]: Một lớp ký tự. Khớp 1 KÝ TỰ DUY NHẤT thuộc (a-z), (A-Z), hoặc (0-9).
#        - {10}: Lượng từ. Yêu cầu lớp ký tự [...] phía trước phải xuất hiện CHÍNH XÁC 10 LẦN.
#    - Kết luận: Chuỗi phải có CHÍNH XÁC 10 KÝ TỰ, và tất cả chỉ được là chữ cái hoặc số.
#
# 6. $
#    - Ý nghĩa: Ký tự "neo" (anchor).
#    - Giải thích: Khẳng định rằng sự so khớp phải kết thúc NGAY TẠI CUỐI CHUỖI.
#
# --- TỔNG KẾT CÁC QUY TẮC ---
#
# Để một chuỗi UID được coi là HỢP LỆ, nó phải thỏa mãn TẤT CẢ các điều kiện sau:
#
# 1. Độ dài: Phải có CHÍNH XÁC 10 ký tự.
# 2. Ký tự cho phép: Chỉ được chứa chữ cái (a-z, A-Z) và số (0-9).
# 3. Chữ hoa: Phải có ÍT NHẤT 2 ký tự IN HOA.
# 4. Số: Phải có ÍT NHẤT 3 ký tự SỐ.
# 5. Tính duy nhất: KHÔNG được có bất kỳ ký tự nào lặp lại.
#
# --- VÍ DỤ ---
#
# * HỢP LỆ:
#   - `AB123cde4f` (10 ký tự, 2 hoa, 4 số, không lặp)
#   - `Abc123Def4` (10 ký tự, 3 hoa, 4 số, không lặp)
#
# * KHÔNG HỢP LỆ:
#   - `AB123cde4A` (Lỗi 5: 'A' lặp lại)
#   - `Ab123cde4f` (Lỗi 3: chỉ 1 chữ hoa)
#   - `AB12cde4fG` (Lỗi 4: chỉ 2 số)
#   - `AB123cde4f5` (Lỗi 1: dài 11 ký tự)
#   - `AB123-de4f` (Lỗi 2: chứa ký tự đặc biệt '-')
#
            
n = int(input())   
for _ in range(n):
    UID = input()
    check = str(bool(re.match(UID_format, UID)))
    if check == 'True':
        print('Valid')
    else:
        print('Invalid')