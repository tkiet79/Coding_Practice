# ==========================================
# MẠNG NƠ-RON ĐA TẦNG (MULTI-LAYER NEURAL NETWORK)
# Xây dựng Forward Pass bằng Pure Python
# ==========================================

def relu(val):
    return max(0, val)

# 1. DỮ LIỆU ĐẦU VÀO (Input Layer)
# x1: 3 phòng ngủ | x2: 10 năm tuổi
x1 = 3.0
x2 = 10.0

print(f"--- INPUT LAYER ---")
print(f"Phòng ngủ: {x1}, Tuổi nhà: {x2}\n")

# ==========================================
# 2. TẦNG ẨN (Hidden Layer) - Gồm 2 Nơ-ron
# ==========================================
# Nơ-ron 1 (Nhiệm vụ: Tìm ra đặc trưng A)
w11 = 0.5  # Trọng số của x1 vào nơ-ron 1
w12 = -0.2 # Trọng số của x2 vào nơ-ron 1
h1_raw = (w11 * x1) + (w12 * x2)

# Nơ-ron 2 (Nhiệm vụ: Tìm ra đặc trưng B)
w21 = -0.4 # Trọng số của x1 vào nơ-ron 2
w22 = 0.8  # Trọng số của x2 vào nơ-ron 2
h2_raw = (w21 * x1) + (w22 * x2)

# ------------------------------------------
# YOUR TURN: ÁP DỤNG HÀM KÍCH HOẠT (ACTIVATION)
# ------------------------------------------
# Hãy cho h1_raw và h2_raw đi qua hàm relu() ở trên!
h1_activated = relu(h1_raw)
h2_activated = relu(h2_raw)

print(f"--- HIDDEN LAYER ---")
print(f"Nơ-ron 1 (Thô): {h1_raw:.2f} | Kích hoạt (ReLU): {h1_activated}")
print(f"Nơ-ron 2 (Thô): {h2_raw:.2f} | Kích hoạt (ReLU): {h2_activated}\n")

# ==========================================
# 3. TẦNG ĐẦU RA (Output Layer) - Gồm 1 Nơ-ron
# ==========================================
# Tầng này nhận đầu vào là kết quả ĐÃ KÍCH HOẠT của tầng ẩn!
w_out1 = 1.5 # Trọng số từ Nơ-ron 1 tới Output
w_out2 = 2.0 # Trọng số từ Nơ-ron 2 tới Output

# ------------------------------------------
# YOUR TURN: TÍNH TOÁN DỰ ĐOÁN CUỐI CÙNG
# ------------------------------------------
# Gợi ý: Nó là Tích vô hướng (Dot Product) của trọng số đầu ra (w_out)
# và giá trị ĐÃ KÍCH HOẠT từ tầng ẩn (h_activated).
# VÀ NHỚ QUY TẮC VÀNG: KHÔNG DÙNG RELU Ở ĐÂY!

final_prediction = h1_activated * w_out1 + h2_activated * w_out2

print(f"--- OUTPUT LAYER ---")
print(f"Dự đoán giá nhà cuối cùng: {final_prediction}")