# 1. Nhập OrderedDict từ thư viện 'collections'
# OrderedDict là một dictionary đặc biệt, nó GHI NHỚ
# thứ tự mà bạn đã thêm các key vào.
from collections import OrderedDict

# 2. Đọc số lượng từ (N)
N = int(input())

# 3. Khởi tạo một OrderedDict rỗng
# Chúng ta sẽ dùng nó để lưu: {"từ": số_lần_đếm}
# Ví dụ: {"bcdef": 2, "abcdefg": 1, "bcde": 1}
word_counts = OrderedDict()

# 4. Lặp N lần để đọc từng từ
for _ in range(N):
    word = input()
    
    # 5. Đây là dòng "ma thuật" để đếm:
    #
    #    word_counts.get(word, 0):
    #    - Lấy giá trị đếm hiện tại của 'word'.
    #    - Nếu 'word' CHƯA CÓ trong dict, trả về giá trị mặc định là 0.
    #
    #    + 1:
    #    - Cộng 1 vào giá trị đếm (hoặc 0+1 nếu là từ mới).
    #
    #    word_counts[word] = ...
    #    - Gán giá trị đếm mới trở lại vào dict.
    #
    #    Quan trọng: Nếu 'word' là mới, OrderedDict sẽ thêm nó
    #    vào CUỐI danh sách, giữ đúng thứ tự xuất hiện.
    word_counts[word] = word_counts.get(word, 0) + 1

# --- XUẤT KẾT QUẢ ---

# 6. Dòng 1: In ra số lượng từ *duy nhất* (distinct).
#    Đây chính là số lượng key có trong dictionary.
print(len(word_counts))

# 7. Dòng 2: In ra số lần đếm, theo đúng thứ tự.
#    .values() -> Lấy ra tất cả các giá trị (số đếm), ví dụ: [2, 1, 1]
#    * -> Dấu * (gọi là "splat" operator) sẽ "mở gói"
#                 danh sách này và truyền vào hàm print.
#                 print(*[2, 1, 1]) tương đương print(2, 1, 1)
print(*word_counts.values())