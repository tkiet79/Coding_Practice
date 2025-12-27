# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Cây rỗng thì coi như đối xứng
        if not root:
            return True
        
        # Gọi hàm phụ để so sánh nhánh trái và nhánh phải
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        # 1. Nếu cả 2 đều None -> Đối xứng (giống nhau ở chỗ cùng không có gì)
        if not t1 and not t2:
            return True
        
        # 2. Nếu 1 bên có, 1 bên không -> Lệch -> False
        if not t1 or not t2:
            return False
            
        # 3. Kiểm tra giá trị VÀ đệ quy kiểm tra con cái
        # Lưu ý quy tắc đối xứng:
        # - t1.left so với t2.right (Ngoài cùng)
        # - t1.right so với t2.left (Trong cùng)
        return (t1.val == t2.val) and \
               self.isMirror(t1.left, t2.right) and \
               self.isMirror(t1.right, t2.left)