#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # Tạo mảng đánh dấu, +1 để dùng index từ 1 đến leaves cho dễ hiểu
        visited = [False] * (leaves + 1)
    
    # Sắp xếp hoặc dùng set để loại bỏ ếch trùng nhau nếu cần, 
    # nhưng thuật toán dưới đã tự xử lý việc đó.
    
        for strength in frogs:
        # 1. Nếu sức mạnh > số lá -> Nhảy qua luôn, bỏ qua
        # 2. Nếu visited[strength] == True -> Nghĩa là đã có con ếch nhỏ hơn 
        #    (là ước của số này) đã nhảy qua các vị trí của con này rồi -> Bỏ qua
            if strength <= leaves and not visited[strength]:
            # Đánh dấu các bội số: strength, 2*strength, 3*strength...
                for j in range(strength, leaves + 1, strength):
                    visited[j] = True
                
    # Đếm số lá chưa được thăm (vẫn là False)
    # Lưu ý: đếm từ 1 đến leaves
        count = 0
        for i in range(1, leaves + 1):
            if not visited[i]:
                count += 1
            
        return count
        
            