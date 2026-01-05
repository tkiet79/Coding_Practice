def find4Numbers(A, N, X):
    # 1. Sắp xếp mảng
    A.sort()
    
    # 2. Hai vòng lặp cố định 2 số đầu
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            
            # Tính phần còn thiếu
            target_2_sum = X - (A[i] + A[j])
            
            # 3. Two Pointers để tìm 2 số còn lại
            left = j + 1
            right = N - 1
            
            while left < right:
                current_2_sum = A[left] + A[right]
                
                if current_2_sum == target_2_sum:
                    return True # Đã tìm thấy
                elif current_2_sum < target_2_sum:
                    left += 1 # Cần tổng lớn hơn
                else:
                    right -= 1 # Cần tổng nhỏ hơn
                    
    return False # Chạy hết vòng lặp mà không thấy
    

