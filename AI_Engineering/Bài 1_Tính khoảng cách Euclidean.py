import numpy as np

def calculate_euclidean_distance(matrix_a, matrix_b):
    # Theo thứ tự: Trừ -> Bình phương -> Tổng theo hàng -> Căn bậc hai.
    return np.sqrt(np.sum(np.square(matrix_a - matrix_b), axis=1))

vector_A = np.random.rand(1000, 50)
vector_B = np.random.rand(1000, 50)
res = calculate_euclidean_distance(vector_A, vector_B)
print(res.shape)
