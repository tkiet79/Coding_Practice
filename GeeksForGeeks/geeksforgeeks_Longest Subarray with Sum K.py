class Solution:
    def longestSubarray(self, arr, k):  
        # Dictionary lưu {tổng_cộng_dồn: chỉ_số_đầu_tiên}
        # Khởi tạo {0: -1} rất quan trọng để xử lý trường hợp dãy con bắt đầu từ index 0
        sum_map = {0: -1} 
        
        current_sum = 0
        max_len = 0
        
        for i, num in enumerate(arr):
            current_sum += num
            
            # 1. Kiểm tra xem phần bù (current_sum - k) đã từng xuất hiện chưa
            if (current_sum - k) in sum_map:
                length = i - sum_map[current_sum - k]
                max_len = max(max_len, length)
            
            # 2. Lưu tổng hiện tại vào map nếu nó chưa từng xuất hiện
            # (Giữ lại chỉ số xuất hiện sớm nhất để đoạn con dài nhất)
            if current_sum not in sum_map:
                sum_map[current_sum] = i
                
        return max_len




