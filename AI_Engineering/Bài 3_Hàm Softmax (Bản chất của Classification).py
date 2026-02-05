import numpy as np


def softmax(Z):
    # 1. Tính e mũ Z (NumPy tính cho toàn bộ phần tử)
    exp_Z = np.exp(Z)
    
    # 2. Tính tổng theo hàng ngang (axis=1)
    # CỰC KỲ QUAN TRỌNG: Phải dùng keepdims=True để giữ shape (N, 1) 
    # thì mới thực hiện phép chia (N, C) / (N, 1) được (Broadcasting)
    sum_exp_Z = np.sum(exp_Z, axis=1, keepdims=True)

    # 3. Chia để ra xác suất
    return exp_Z / sum_exp_Z

Z = np.random.randn(10, 3)
probs = softmax(Z)
print(np.multiply(probs,100))