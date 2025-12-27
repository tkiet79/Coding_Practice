# bước 1: Nhập thư viện NumPy và đặt tên viết tắt là np, giúp truy cập các hàm xử lý mảng/ma trận hiệu quả.
# Và Nhập thư viện toán học chuẩn của Python để sử dụng hàm sqrt (căn bậc hai).
import numpy as np
import math

# bước 2: tạo ma trận A,B,C với hàm np.array()
# np.random.randint(start, end, size): Hàm sinh ma trận số nguyên ngẫu nhiên.
#     start: Giá trị bắt đầu.
#     end: Giá trị kết thúc (không bao gồm số này).
#     size=(rows, cols): Kích thước bảng (số hàng, số cột).
#     các ma trận B,C tương tự
A = np.random.randint(1, 101, size=(10, 10))
B = np.random.randint(1, 101, size=(2, 10))
C = np.random.randint(1, 101, size=(10, 2))

print("Ma trận A:")
print(A)
print()
print("Ma trận B:")
print(B)
print()
print("Ma trận C:")
print(C)
print()

print("CÂU A: tính A + A^T + CB + B^T C^T")
print()
result = (A + A.T) + (C @ B) + (B.T @ C.T) #toán tử @ là phép nhân ma trận chuẩn trong đại số tuyến tính: hàng của A nhân với cột của B                                                                
print(result)                              # B.T A.T C.T là các ma trận chuyển vị trong đề bài
print()

print("CÂU B: tính (A/10) + (A/11)^2 +...+ (A/18)^9 + (A/19)^10")
print()
count = np.zeros_like(A, dtype=float) # tạo ra 1 ma trận toàn số 0 với số hàng và số cột giống ma trận A với kiểu dữ liệu float
for i in range(1,11):
    value = np.linalg.matrix_power((A / (9 + i)), i) # np.linalg.matrix_power(): Hàm chuyên dụng của NumPy để tính lũy thừa ma trận (nhân ma trận với chính nó i lần).
    count +=value # Cộng giá trị tính được của bước hiện tại vào tổng chung. 
print(count)
print()

print("CÂU C: tìm và in ra các số lẻ trong ma trận A dưới dạng 1 vector")
print()
#    Phép toán (A % 2 != 0) sẽ được áp dụng cho MỌI phần tử.
#    Nó tạo ra một ma trận 10x10 mới chứa True/False.
#    - True: nếu phần tử ở vị trí đó là số lẻ.
#    - False: nếu phần tử ở vị trí đó là số chẵn.
is_odd = (A % 2 != 0)


#    Khi truyền 'is_odd_mask' vào A, NumPy sẽ chỉ
#    chọn ra các phần tử mà ở đó mask là True.
#    Nó cũng tự động "làm phẳng" (flatten) kết quả
#    thành một vector (mảng 1D) mới.
odd_numbers_vector = A[is_odd]
print(odd_numbers_vector)
print()



print("CÂU E: tìm ra hàng có số lượng số nguyên tố nhiều nhất")
print()
def is_prime(n):
    """Hàm kiểm tra số nguyên tố (chỉ cho n > 0)"""
    # 1 và 0 không phải là số nguyên tố
    if n <= 1:
        return False
    # 2 là số nguyên tố
    if n == 2:
        return True
    # Bất kỳ số chẵn nào khác (ngoại trừ 2) đều không phải số nguyên tố
    if n % 2 == 0:
        return False
    
    # hàm range(start, stop, step) với start là chỉ số bắt đầu, stop là chỉ số dừng lại giá trị cuối cùng sẽ là end - 1, step là số khoảng cách giữa 2 giá trị
    # vì Bất kỳ số chẵn nào khác (ngoại trừ 2) đều không phải số nguyên tố nên ta chỉ xét các số lẻ
    # Nếu chúng ta không tìm thấy ước số nào từ 2 cho đến sqrt(n) (sqrt là căn bậc 2), thì n chắc chắn là số nguyên tố.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    # Nếu không tìm thấy ước số nào, nó là số nguyên tố
    return True

# --- Bước 2: "Vector hóa" hàm is_prime ---
# Biến hàm is_prime (chỉ nhận 1 số) thành một hàm
# có thể hoạt động trên toàn bộ mảng NumPy cùng một lúc.
vectorized_is_prime = np.vectorize(is_prime)

# --- Bước 3: Tạo "mặt nạ" True/False cho ma trận A ---
# Áp dụng hàm đã vector hóa cho toàn bộ ma trận A.
# Kết quả là một ma trận 10x10 chứa True (nếu là SNT) / False (nếu không).
prime_mask = vectorized_is_prime(A)

# --- Bước 4: Đếm số lượng số nguyên tố trên mỗi hàng ---
# 'sum' một mảng boolean sẽ đếm số lượng 'True'.
# axis=1 có nghĩa là tính tổng theo chiều ngang (tức là tính tổng mỗi hàng).
# Kết quả là một vector 1D (dài 10) chứa số đếm cho mỗi hàng.
prime_counts_per_row = np.sum(prime_mask, axis=1)

# --- Bước 5: Tìm số đếm lớn nhất ---
max_prime_count = np.max(prime_counts_per_row)

# --- Bước 6: Lọc và in các hàng kết quả ---
# Đây là "Boolean Indexing"
# Chúng ta muốn lấy các hàng (rows) từ ma trận A ở vị trí vector đếm 'prime_counts_per_row' bằng (==) với giá trị 'max_prime_count'
print(A[prime_counts_per_row == max_prime_count])
print()

print("CÂU D: tìm và in ra các số nguyên tố trong ma trận A dưới dạng 1 vector")
print()
print(A[prime_mask])
print()

print("CÂU F: Tìm các hàng có chuỗi số lẻ liên tục dài nhất")
print()
def get_longest_odd_streak(row_array):
    """
    Hàm này nhận vào một mảng 1D (một hàng) 
    và trả về độ dài của chuỗi số lẻ DÀI NHẤT.
    """
    max_streak = 0      # Độ dài chuỗi dài nhất tìm thấy
    current_streak = 0  # Độ dài chuỗi hiện tại
    
    for num in row_array:
        if num % 2 != 0:
            # Nếu số là lẻ, tăng chuỗi hiện tại
            current_streak += 1
        else:
            # Nếu số là chẵn, chuỗi bị ngắt
            # Cập nhật max_streak nếu chuỗi vừa rồi dài hơn
            max_streak = max(max_streak, current_streak)
            # Reset chuỗi hiện tại về 0
            current_streak = 0
            
    # Kiểm tra lần cuối: Đề phòng trường hợp chuỗi dài nhất
    # nằm ở cuối hàng (không có số chẵn nào ngắt nó)
    max_streak = max(max_streak, current_streak)
    
    return max_streak

# --- Bước 2: Lặp qua từng hàng của A và tính chuỗi dài nhất ---
# (Chúng ta không thể vector hóa hoàn toàn việc này nên dùng vòng lặp for là cách rõ ràng nhất)

streak_counts_per_row = [] # List để lưu độ dài chuỗi của mỗi hàng

# Lặp qua 10 hàng của A
for row in A:
    # row là một mảng 1D (ví dụ: [1, 5, 7, 8, ...])
    # Gọi hàm phụ để tìm chuỗi dài nhất cho hàng này
    longest_streak_in_this_row = get_longest_odd_streak(row)
    
    # Thêm kết quả vào list
    streak_counts_per_row.append(longest_streak_in_this_row)

# Chuyển list kết quả thành mảng NumPy để lọc
streak_counts = np.array(streak_counts_per_row)


# --- Bước 3: Tìm độ dài chuỗi lớn nhất ---
max_streak_length = np.max(streak_counts)

# --- Bước 4: Lọc và in các hàng kết quả ---
# (Logic này giống hệt Câu E, nhưng dùng biến 'streak_counts')
print(A[streak_counts == max_streak_length])
