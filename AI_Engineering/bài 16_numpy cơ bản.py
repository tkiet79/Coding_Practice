import numpy as np

# Tạo dữ liệu mẫu
np.random.seed(10)
matrix = np.random.randint(1, 100, (6, 4)) # Ma trận 6 hàng 4 cột
vector_a = np.array([1, 2, 3, 4])
vector_b = np.array([5, 6, 7, 8])
print("ma trận gốc: \n", matrix)
print("_"*100)
print()
# Câu 1: Truy xuất nâng cao (Slicing)
# Từ matrix, hãy lấy ra một ma trận con gồm 3 hàng đầu tiên và 2 cột cuối cùng.
sub_matrix = matrix[0:3, 2:4]

# Câu 2: Thay đổi hình dạng (Reshaping)
# Biến ma trận matrix (6x4) thành một khối 3D có kích thước (3, 2, 4).
matrix = matrix.reshape(3, 2, 4)

# Câu 3: Tìm kiếm vị trí (Argmax)
# Tìm chỉ số (index) của giá trị lớn nhất trong mỗi hàng của matrix.
max_idx = np.argmax(matrix, axis=1)

