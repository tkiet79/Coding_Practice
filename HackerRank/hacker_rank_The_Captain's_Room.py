#  bị TLE
'''n = int(input())
room_list = list(map(int,input().split()))
room_list.sort()
for value in room_list:
    if room_list.count(value) != n:
        print(value)'''

# tối ưu hóa

n = int(input())
room_list = list(map(int, input().split()))

# Khởi tạo một dict rỗng
counts = {}

# --- Đây là phần tối ưu hóa ---
# Lặp qua danh sách CHỈ MỘT LẦN
for room in room_list:
    # Lấy giá trị đếm hiện tại (hoặc 0 nếu chưa có),
    # sau đó cộng 1 và gán lại.
    counts[room] = counts.get(room, 0) + 1
# --------------------------------

# Lặp qua dict (rất nhanh) để tìm kết quả
for room, count in counts.items():
    if count != n:
        print(room)
        break


    



