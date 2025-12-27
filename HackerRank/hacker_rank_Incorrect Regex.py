import re

T = int(input())

for _ in range(T):
    S = input()
    is_valid = True
    
    # BƯỚC 1: Kiểm tra các lỗi cú pháp chuẩn
    try:
        re.compile(S)
    except re.error:
        is_valid = False
        
    # BƯỚC 2: Nếu Python thấy hợp lệ, kiểm tra các quy tắc tùy chỉnh
    # (cấm các bộ định lượng non-greedy/possessive)
    if is_valid:
        # Tìm một bộ định lượng {*, +, ?}
        # 1. (^[?*+]) - Bắt đầu bằng nó (ví dụ S="+abc")
        # 2. ([^\\][?*+]) - Hoặc, đứng sau một ký tự KHÔNG PHẢI là \
        #
        # Và theo sau nó là một bộ định lượng khác [?*+]
        
        # Mẫu này tìm: [một ký tự ko phải \] + [bộ định lượng] + [bộ định lượng]
        # Ví dụ: 'a*+', 'a++', 'a*?'
        if re.search(r"[^\\][?*+]{2}", S):
            is_valid = False
            
        # Mẫu này tìm: [bắt đầu chuỗi] + [bộ định lượng] + [bộ định lượng]
        # Ví dụ: '++abc', '*?abc'
        elif re.search(r"^[?*+]{2}", S):
             is_valid = False

    # In kết quả
    if is_valid:
        print("True")
    else:
        print("False")