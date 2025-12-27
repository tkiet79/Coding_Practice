from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dòng 1: Tạo từ điển thông minh
        anagram_map = defaultdict(list)
        
        # Dòng 2: Bắt đầu duyệt từng từ
        for s in strs:

            # Dòng 3: Tạo bảng đếm rỗng
            count = [0] * 26

            # Dòng 4: Đếm từng ký tự trong từ hiện tại
            for char in s:

                # Dòng 5: Tính vị trí và tăng đếm
                count[ord(char) - ord('a')] += 1

            # Dòng 6: Biến bảng đếm thành Key và lưu vào map
            key = tuple(count)
            anagram_map[key].append(s)
            
        # Dòng 7: Trả về kết quả
        return list(anagram_map.values())

    

