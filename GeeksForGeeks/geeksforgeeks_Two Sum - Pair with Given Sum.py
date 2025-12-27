class Solution:
	def twoSum(self, arr, target):
	    # Tạo một tập hợp để lưu các số đã đi qua
        seen = set()
        
        for num in arr:
            # Tính số còn thiếu để đủ target
            needed = target - num
            
            # Kiểm tra xem số còn thiếu đã xuất hiện trước đó chưa
            if needed in seen:
                return True
            
            # Nếu chưa, thêm số hiện tại vào tập hợp
            seen.add(num)
            
        return False


    

    
        










