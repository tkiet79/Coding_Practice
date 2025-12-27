# --- Nhập thư viện ---
import re  # Nhập thư viện Regular Expression (Regex)

# --- Lấy Dữ liệu Đầu vào ---
# Yêu cầu người dùng nhập chuỗi lớn (S)
S = input() 
# Yêu cầu người dùng nhập chuỗi con (k) cần tìm
k = input() 

# --- Khởi tạo Biến ---
# Đặt một "biến cờ" (flag) để theo dõi xem chúng ta có tìm thấy bất kỳ
# kết quả nào hay không. Ban đầu, giả định là 'No' (Không).
anymatch = 'No'

# --- Xử lý Chính: Tìm kiếm bằng Regex ---

# Sử dụng re.finditer để tìm TẤT CẢ các vị trí khớp với mẫu regex.
# Vòng lặp 'for' sẽ chạy qua từng kết quả (match object 'm') mà finditer tìm thấy.
#
# PHÂN TÍCH MẪU REGEX: r'(?=('+k+'))'
# Giả sử k = "aa", mẫu sẽ trở thành r'(?=(aa))'
#
# 1. r'...' : Đây là một "raw string" (chuỗi thô). 
#    Nó bảo Python không xử lý các ký tự đặc biệt như '\' (escape). Rất quan trọng cho regex.
#
# 2. (?=...) : Đây là "Positive Lookahead" (Nhìn về phía trước).
#    - Nó hoạt động như một cửa sổ "nhìn trộm". Nó kiểm tra xem mẫu bên trong nó (tức là 'aa')
#      có tồn tại ở vị trí hiện tại hay không.
#    - QUAN TRỌNG: Nó KHÔNG "tiêu thụ" (consume) ký tự. Nó chỉ nhìn rồi lùi lại.
#      Điều này cho phép vòng lặp tìm kiếm tiếp ở vị trí TIẾP THEO (vị trí 1), 
#      thay vì nhảy qua ký tự đã khớp (vị trí 2). Đây chính là mấu chốt để
#      tìm thấy các chuỗi TRÙNG LẶP (overlapping).
#
# 3. (...) bên trong: (?=(aa))
#    - Dấu ngoặc đơn bao quanh 'aa' tạo thành một "Capturing Group" (nhóm bắt giữ), hay group(1).
#    - Mặc dù Lookahead không "tiêu thụ" ký tự, group bên trong nó vẫn "bắt giữ"
#      lại chuỗi mà nó nhìn thấy. Đây là cách chúng ta lấy được vị trí start/end.
#
for m in re.finditer(r'(?=('+k+'))', S):
    
    # Nếu vòng lặp 'for' này được chạy (nghĩa là finditer tìm thấy ít nhất 1 kết quả),
    # chúng ta lập tức gạt cờ 'anymatch' thành 'Yes'.
    anymatch = 'Yes'
    
    # 'm' là đối tượng kết quả (match object).
    # m.start(1): Lấy vị trí BẮT ĐẦU của group(1) (chính là chuỗi 'k').
    # m.end(1): Lấy vị trí KẾT THÚC của group(1). 
    #           (Lưu ý: vị trí end luôn là chỉ số SAU ký tự cuối cùng).
    #
    # Ví dụ: chuỗi "aa" ở đầu (chỉ số 0 và 1) sẽ có start(1)=0 và end(1)=2.
    # Đề bài thường muốn chỉ số của ký tự cuối (tức là 1), nên ta dùng end(1) - 1.
    print((m.start(1), m.end(1) - 1))

# --- In Kết quả Cuối cùng ---

# Sau khi vòng lặp kết thúc, kiểm tra biến cờ 'anymatch'.
# Nếu nó vẫn là 'No' (nghĩa là vòng lặp 'for' không bao giờ chạy),
# thì in ra (-1, -1) theo yêu cầu.
if anymatch == 'No':
    print((-1, -1))