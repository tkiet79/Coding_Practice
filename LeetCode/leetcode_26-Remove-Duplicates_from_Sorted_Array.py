class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Trường hợp mảng rỗng
        if not nums:
            return 0
        
        # Con trỏ k dùng để chốt vị trí các số duy nhất
        # Bắt đầu từ 1 vì phần tử đầu tiên (index 0) luôn luôn là duy nhất
        k = 1
        
        # Duyệt từ phần tử thứ 2 trở đi
        for i in range(1, len(nums)):
            # Nếu thấy số hiện tại KHÁC số liền trước nó
            # Nghĩa là ta tìm thấy một số mới (không trùng)
            if nums[i] != nums[i-1]:
                # Ghi đè số mới này vào vị trí k
                nums[k] = nums[i]
                # Tăng k lên để chờ ghi số tiếp theo
                k += 1
        
        # Trả về k (chính là số lượng phần tử duy nhất)
        return k