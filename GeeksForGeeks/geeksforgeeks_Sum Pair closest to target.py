class Solution:
    def sumClosest(self, arr, target):
        # Kiểm tra điều kiện đầu vào
        if len(arr) < 2:
            return []
        
        # Sắp xếp mảng để dùng Two Pointers
        arr.sort()
        
        left = 0
        right = len(arr) - 1
        
        # Khởi tạo giá trị ban đầu
        min_diff = float('inf')  # Khoảng cách nhỏ nhất tìm thấy
        res = []                 # Cặp kết quả
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            # Tính khoảng cách hiện tại tới target
            current_diff = abs(current_sum - target)
            
            # TRƯỜNG HỢP 1: Tìm thấy khoảng cách nhỏ hơn kỉ lục cũ
            if current_diff < min_diff:
                min_diff = current_diff
                res = [arr[left], arr[right]]
            
            # TRƯỜNG HỢP 2: Khoảng cách bằng kỉ lục cũ (Tie-breaking)
            # Đề bài yêu cầu: Lấy cặp có "maximum absolute difference" (hiệu lớn nhất)
            elif current_diff == min_diff:
                # Trong mảng đã sort, hiệu (b-a) chính là (arr[right] - arr[left])
                current_abs_diff = arr[right] - arr[left]
                if res: # Đảm bảo res không rỗng
                    old_abs_diff = res[1] - res[0]
                    if current_abs_diff > old_abs_diff:
                        res = [arr[left], arr[right]]
            
            # Di chuyển con trỏ để tìm tổng khác gần target hơn
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Nếu current_sum == target, đây chắc chắn là cặp gần nhất (diff = 0)
                # Vì mảng đã sort và ta đi từ 2 phía, cặp đầu tiên thấy diff=0 
                # sẽ có hiệu lớn nhất. Return luôn.
                return [arr[left], arr[right]]
                
        return res