class Solution:
    def minDist(self, arr, x, y):
        idx_x = -1
        idx_y = -1
        min_dist = float('inf') # KHAI BÁO GIÁ TRỊ BAN ĐẦU LÀ DƯƠNG VÔ CÙNG VÌ KHI SO SÁNH THÌ MỌI SỐ SẼ NHỎ HƠN NÓ
        
        for i in range(len(arr)):
            if arr[i] == x:
                idx_x = i
                if idx_y != -1:
                    min_dist = min(min_dist, abs(idx_x - idx_y))
            
            elif arr[i] == y:
                idx_y = i
                if idx_x != -1:
                    min_dist = min(min_dist,abs(idx_x - idx_y))
            
        if min_dist == float('inf'):
            return -1
        return min_dist
                    
        
            
        
        
                
      
        