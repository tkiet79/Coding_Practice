regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	
''''
 # 1. NEO BẮT ĐẦU: Phải khớp từ đầu chuỗi
    
    # 2. PHẦN HÀNG NGHÌN: (0-3000)
    M{0,3}                 #    Khớp 0, 1, 2, hoặc 3 chữ 'M' (1000)
                           #    (ví dụ: M, MM, MMM)
                           
    # 3. PHẦN HÀNG TRĂM: (0-900)
    (                      #    Bắt đầu nhóm cho hàng trăm
        CM                 #    Khớp 'CM' (900)
        |                  #    HOẶC
        CD                 #    Khớp 'CD' (400)
        |                  #    HOẶC
        D?C{0,3}           #    Khớp các trường hợp còn lại:
                           #    D?     -> 'D' (500) có thể có (1) hoặc không (0)
                           #    C{0,3} -> 'C' (100) có thể lặp 0-3 lần
                           #    (Kết hợp: D, DC, DCC, DCCC (500-800)
                           #     hoặc C, CC, CCC (100-300) hoặc rỗng (0))
    )                      #    Kết thúc nhóm hàng trăm
                           
    # 4. PHẦN HÀNG CHỤC: (0-90)
    (                      #    Bắt đầu nhóm cho hàng chục
        XC                 #    Khớp 'XC' (90)
        |                  #    HOẶC
        XL                 #    Khớp 'XL' (40)
        |                  #    HOẶC
        L?X{0,3}           #    Khớp các trường hợp còn lại:
                           #    L?     -> 'L' (50) có thể có hoặc không
                           #    X{0,3} -> 'X' (10) có thể lặp 0-3 lần
                           #    (Kết hợp: L, LX, LXX, LXXX (50-80)
                           #     hoặc X, XX, XXX (10-30) hoặc rỗng (0))
    )                      #    Kết thúc nhóm hàng chục
                           
    # 5. PHẦN HÀNG ĐƠN VỊ: (0-9)
    (                      #    Bắt đầu nhóm cho hàng đơn vị
        IX                 #    Khớp 'IX' (9)
        |                  #    HOẶC
        IV                 #    Khớp 'IV' (4)
        |                  #    HOẶC
        V?I{0,3}           #    Khớp các trường hợp còn lại:
                           #    V?     -> 'V' (5) có thể có hoặc không
                           #    I{0,3} -> 'I' (1) có thể lặp 0-3 lần
                           #    (Kết hợp: V, VI, VII, VIII (5-8)
                           #     hoặc I, II, III (1-3) hoặc rỗng (0))
    )                      #    Kết thúc nhóm hàng đơn vị
                           
    #$                     # 6. NEO KẾT THÚC: Phải khớp đến cuối chuỗi'''


import re
print(str(bool(re.match(regex_pattern, input()))))