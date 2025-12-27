class Solution:
    """
    Tìm Tiền tố chung dài nhất (Longest Common Prefix) trong một danh sách chuỗi.
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Xử lý trường hợp danh sách rỗng (Empty list)
        if not strs:
            return ""

        # Tối ưu hóa: Tìm chuỗi ngắn nhất. LCP không thể dài hơn chuỗi này.
        shortest_str = min(strs, key=len)
        
        # Biến cờ (Flag) để báo hiệu khi tìm thấy sự khác biệt
        mismath_found = False
        
        # Vòng lặp Ngoài (Duyệt theo chỉ mục/cột): Duyệt qua từng ký tự của chuỗi ngắn nhất
        for i in range(len(shortest_str)):
            
            # Ký tự Tham Chiếu: Lấy ký tự tại chỉ mục i từ chuỗi ngắn nhất
            char_to_check = shortest_str[i]
            
            # Vòng lặp Trong (So sánh theo hàng): Lặp qua tất cả các chuỗi trong danh sách
            for other_str in strs:
                
                # Logic Khác Biệt (Mismatch): Nếu ký tự không khớp
                if other_str[i] != char_to_check:
                    
                    # Tìm LCP: Lấy chuỗi con từ đầu đến vị trí ngay trước vị trí lỗi (i)
                    lcp_result = shortest_str[:i]
                    
                    # Đặt cờ báo lỗi và thoát vòng lặp trong
                    mismath_found = True
                    break
                    
            # Thoát Sớm (Outer Loop): Nếu cờ đã được kích hoạt, thoát khỏi vòng lặp chính
            if mismath_found:
                # Trả về kết quả đã tính được (lcp_result)
                return lcp_result
        
        # Trường hợp LCP = Chuỗi Ngắn Nhất: Nếu vòng lặp chính hoàn thành mà không tìm thấy lỗi, 
        # điều đó có nghĩa là chuỗi ngắn nhất chính là tiền tố chung.
        return shortest_str