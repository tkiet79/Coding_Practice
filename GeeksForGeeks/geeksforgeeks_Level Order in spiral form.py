'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

from collections import deque

class Solution:
    def findSpiral(self, root):
        if root is None:
            return []
        
        result = []
        queue = deque([root]) # Khởi tạo queue với root
        
        level = 0
        
        while queue:
            size = len(queue)
            current_level = []
            
            for _ in range(size):
                node = queue.popleft()
                
                # Quan trọng: Lấy data để in ra
                current_level.append(node.data)
                
                # Quan trọng: Thêm con vào hàng đợi (Trái trước Phải sau)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Logic xoắn ốc: Tầng chẵn thì đảo ngược danh sách kết quả của tầng đó
            if level % 2 == 0:
                current_level.reverse()
                
            result.extend(current_level)
            level += 1
            
        return result
        