import sys

# 1. Đọc dữ liệu nhanh (Fast I/O)
input_data = sys.stdin.read().split()
if not input_data:
    exit()

iterator = iter(input_data)
n = int(next(iterator))
capacity = int(next(iterator))

# Đọc mảng a (refuels) và b (costs)
# Lưu ý: refuels thực tế là a[i], nhưng bị giới hạn bởi capacity ngay từ đầu vào
refuels = [min(int(next(iterator)), capacity) for _ in range(n)]
costs = [int(next(iterator)) for _ in range(n)]

# 2. Tính chênh lệch ban đầu (Net gain/loss)
diff = [refuels[i] - costs[i] for i in range(n)]

# 3. NHÂN ĐÔI MẢNG để xử lý tính chất vòng tròn
# Giúp thuật toán "nhìn thấy" được tương lai xuyên qua điểm cuối mảng
refuels = refuels * 2
diff = diff * 2 

cnt = 0

# 4. Duyệt ngược từ 2*n - 1 về 0
# Logic: diff[i] sẽ lưu mức xăng thấp nhất (tương đối) mà ta sẽ chạm đáy
# nếu xuất phát từ i và đi về phía trước.
for i in range(2 * n - 1, -1, -1):
    # Nếu i là phần tử cuối cùng, không có "người sau" để cộng dồn
    if i == 2 * n - 1:
        current_min = diff[i]
    else:
        # Công thức quan trọng:
        # Mức thấp nhất mới = min(mức thay đổi tại chỗ, mức thay đổi tại chỗ + mức thấp nhất của chặng sau)
        current_min = min(diff[i], diff[i] + diff[i+1])
    
    diff[i] = current_min

    # Chỉ đếm kết quả cho vòng lặp đầu tiên (0 đến n-1)
    if i < n:
        # Điều kiện 1: diff[i] >= 0 nghĩa là không bao giờ bị âm xăng
        # Điều kiện 2: (refuels[i] - diff[i]) <= capacity nghĩa là 
        # lượng xăng cần tích trữ để bù cho đáy sâu nhất không vượt quá dung tích bình.
        if diff[i] >= 0 and (refuels[i] - diff[i] <= capacity):
            cnt += 1

print(cnt)