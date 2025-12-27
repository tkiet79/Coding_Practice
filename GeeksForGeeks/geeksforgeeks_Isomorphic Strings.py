class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
            
        map1 = {} # Sổ chiều đi
        map2 = {} # Sổ chiều về
        
        # Duyệt từng cặp ký tự (ví dụ: a-x, a-x, b-y)
        for c1, c2 in zip(s1, s2):
            
            # 1. Kiểm tra chiều đi: c1 đã từng xuất hiện chưa?
            if c1 in map1:
                # Nếu có, kiểm tra xem "người cũ" có phải là c2 không?
                if map1[c1] != c2:
                    return False # Sai vì c1 đổi lòng đổi dạ
            else:
                # Nếu chưa, kiểm tra xem c2 đã bị ai xí phần chưa (chiều về)
                if c2 in map2:
                    return False # Sai vì c2 đã thuộc về người khác
                
                # Nếu cả 2 đều mới tinh -> Ghi vào sổ
                map1[c1] = c2
                map2[c2] = c1
                
        return True