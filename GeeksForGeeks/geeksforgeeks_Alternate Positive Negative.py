class Solution:
    def rearrange(self, arr):
        res = []
        positive_num = [val for val in arr if val >= 0]
        negative_num = [val for val in arr if val < 0]
        
        # Lấy độ dài tối thiểu để ghép cặp
        i = 0
        j = 0
        
        # Vòng lặp ghép xen kẽ (chạy đến khi một trong hai bên hết hàng)
        while i < len(positive_num) and j < len(negative_num):
            res.append(positive_num[i])
            i += 1
            res.append(negative_num[j])
            j += 1
            
        # QUAN TRỌNG: Nối nốt phần còn thừa vào cuối
        # Nếu positive còn thừa
        if i < len(positive_num):
            res.extend(positive_num[i:])
            
        # Nếu negative còn thừa
        if j < len(negative_num):
            res.extend(negative_num[j:])
        
        arr[:] = res
        return arr