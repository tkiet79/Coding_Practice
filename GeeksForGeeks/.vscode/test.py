#User function Template for python3
from typing import List
class Solution:
    def binary_search(self, arr: List[int], target: int) -> int:
        """
        Hàm helper thực hiện Binary Search tìm cận trên (Upper Bound).
        Mục tiêu: Tìm vị trí index đầu tiên mà tại đó arr[index] > target.
        Vị trí này cũng chính là số lượng các phần tử trong arr nhỏ hơn hoặc bằng target.
        
        Ví dụ: arr = [1, 2, 4, 4, 5], target = 4
        - Các số <= 4 là: 1, 2, 4, 4 (tổng 4 số)
        - Vị trí đầu tiên > 4 là số 5 (index 4)
        -> Trả về 4.
        """
        low = 0
        high = len(arr) # Lưu ý: high là len(arr), không phải len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] <= target:
                # Nếu phần tử giữa vẫn nhỏ hơn hoặc bằng target,
                # nghĩa là đáp án nằm ở phía bên phải (không bao gồm mid hiện tại).
                # Ta cần tìm cái lớn hơn hẳn target cơ.
                low = mid + 1
            else:
                # Nếu arr[mid] > target, thì mid có thể là đáp án,
                # hoặc đáp án nằm bên trái mid.
                high = mid
                
        return low
    def countElements(self, a: List[int], b: List[int], n: int, query: List[int], q: int) -> List[int]:
        if not b:
            return [0] * q
        
        # BƯỚC 1: Pre-processing
        # Vẫn phải sort. Tự viết QuickSort/MergeSort cũng được nhưng Python sort (Timsort) quá tốt rồi.
        # Ở đây tao giữ lại b.sort() vì bài toán mày hỏi là về tìm kiếm, không phải sắp xếp.
        b.sort()
        
        results = []
        
        # BƯỚC 2: Processing Queries
        for idx in query:
            # Edge case handling
            if idx < 0 or idx >= len(a):
                results.append(0)
                continue
                
            target = a[idx]
            
            # Thay vì dùng bisect.bisect_right(b, target), gọi hàm tự viết
            count = self.binary_search(b, target)
            
            results.append(count)
            
        return results
        
                    