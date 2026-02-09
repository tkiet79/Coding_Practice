import numpy as np

# Tạo dữ liệu mẫu
np.random.seed(10)
matrix = np.random.randint(1, 100, (6, 4)) # Ma trận 6 hàng 4 cột
vector_a = np.array([1, 2, 3, 4])
vector_b = np.array([5, 6, 7, 8])
print("ma trận gốc: \n", matrix)
print()
print("_"*100)
print()
# Câu 1: Truy xuất nâng cao (Slicing)
# Từ matrix, hãy lấy ra một ma trận con gồm 3 hàng đầu tiên và 2 cột cuối cùng.
print("Câu 1: Truy xuất nâng cao (Slicing)")
print()
sub_matrix = matrix[0:3, 2:4]
print(sub_matrix)
print("_"*100)
print()

# Câu 2: Thay đổi hình dạng (Reshaping)
# Biến ma trận matrix (6x4) thành một khối 3D có kích thước (3, 2, 4).
print("câu 2: Thay đổi hình dạng (Reshaping)")
print()
matrix = matrix.reshape(3, 2, 4)
print(matrix)
print("_"*100)
print()

# Câu 3: Tìm kiếm vị trí (Argmax)
# Tìm chỉ số (index) của giá trị lớn nhất trong mỗi hàng của matrix.
print("câu 3: Tìm kiếm vị trí (Argmax)")
print()
max_idx = np.argmax(matrix, axis=1)
print(max_idx)
print("_"*100)
print()

# Câu 4: Broadcasting cơ bản
#Lấy matrix trừ đi vector_a. (Gợi ý: Kiểm tra xem kích thước có khớp để trừ theo hàng không).
print("Câu 4: Broadcasting cơ bản")
print()
res = matrix - vector_a
print(res)
print("_"*100)
print()


# Câu 5: Lọc dữ liệu theo điều kiện (Boolean Masking)
# Tìm tất cả các số trong matrix là số chẵn và lớn hơn 50. Thay thế chúng bằng số 0.
print("Câu 5: Lọc dữ liệu theo điều kiện (Boolean Masking)")
print()
matrix[(matrix % 2 ==0) & (matrix > 50)] = 0
print(matrix)
print("_"*100)
print()

# Câu 6: Thống kê đa chiều
# Tính giá trị trung bình của mỗi cột và độ lệch chuẩn (Standard Deviation) của toàn bộ ma trận.
print("Câu 6: Thống kê đa chiều")
print()
revenue_value_cols = np.mean(matrix, axis=0)
print(revenue_value_cols)
print()
Standard_Deviation = np.std(matrix)
print(Standard_Deviation)
print("_"*100)
print()

# Câu 7: Kết hợp mảng (Stacking)
# Gộp vector_a và thành một ma trận mới có 2 hàng vector_b  (Dùng np.vstack).
# Sau đó gộp chúng thành một ma trận có 8 phần tử nằm trên 1 hàng ngang (Dùng np.concatenate)
print("Câu 7: Kết hợp mảng (Stacking)")
print()
combie_matrix = np.vstack((vector_a, vector_b))
print(combie_matrix)
combie_matrix = np.concatenate(combie_matrix)
print(combie_matrix)
print("_"*100)
print()

# Câu 8: Sắp xếp (Sorting)
# Sắp xếp các phần tử trong mỗi hàng của matrix theo thứ tự tăng dần.
print("Câu 8: Sắp xếp (Sorting)")
matrix = np.sort(matrix, axis=1)
print(matrix)
print("_"*100)
print()

# Câu 9: Tích vô hướng (Dot Product)
# Tính tích vô hướng của vector_a và vector_b. (Kết quả phải là một con số duy nhất).
print("Câu 9: Tích vô hướng (Dot Product)")
print()
Dot_Product = np.dot(vector_a, vector_b)
print(Dot_Product)
print("_"*100)
print()

# Câu 10: Xử lý giá trị lỗi (NaN)
# Tạo một mảng có 5 phần tử, trong đó có 2 phần tử là np.nan. 
# Viết code để tính trung bình của mảng đó mà bỏ qua các giá trị nan (Gợi ý: Dùng np.nanmean).
print("Câu 10: Xử lý giá trị lỗi (NaN)")
print()
arr = np.array([3,7,np.nan, 374, np.nan])
print(arr)
print()
result = np.nanmean(arr)
print(result)
print("_"*100)
print()
print("-"*45, "END", "-"*45)

