import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. TRIỆU HỒI DỮ LIỆU ---
try:
    df = pd.read_csv('Smartphone_Usage_Productivity_Dataset_50000.csv')
    print("--- ĐÃ TẢI DỮ LIỆU SMARTPHONE THÀNH CÔNG ---")
except:
    print("--- LỖI: KHÔNG TÌM THẤY FILE ---")

# =========================================================================
# THUẬT NGỮ CỐT LÕI (GLOSSARY)
# =========================================================================
# User_ID:                  ID định danh người dùng.
# Occupation:               Nghề nghiệp (Student, Professional, Freelancer, etc.).
# Daily_Phone_Hours:        Tổng số giờ sử dụng điện thoại mỗi ngày.
# Social_Media_Hours:       Số giờ dành cho mạng xã hội mỗi ngày.
# Work_Productivity_Score:  Điểm năng suất công việc (thường từ 1-10).
# Sleep_Hours:              Số giờ ngủ mỗi đêm.
# Stress_Level:             Mức độ căng thẳng cảm nhận (thường từ 1-10).
# App_Usage_Count:          Số lượng ứng dụng sử dụng trong ngày.
# Caffeine_Intake_Cups:     Số ly thức uống chứa caffeine (cà phê, trà) mỗi ngày.
# Weekend_Screen_Time:      Thời gian sử dụng màn hình vào cuối tuần.
# =========================================================================

# =========================================================================
# KHUNG SƯỜN 15 NHIỆM VỤ (LEVEL: DATA SCIENTIST)
# =========================================================================

# --- NHÓM 1: THỐNG KÊ MÔ TẢ & NHÂN KHẨU HỌC (CÂU 1 - 4) ---
# Câu 1: Kiểm tra thông tin tổng quát (info, describe) và kiểm tra dữ liệu thiếu.
def cau_1():
    print(df.info())
    print(df.isnull().sum())
    print(df.describe())

# Câu 2: Vẽ biểu đồ phân phối độ tuổi (Age) của người dùng trong bộ dữ liệu.
def cau_2():
    df['age_quantity'] = df['Gender'].value_counts()
    plt.figure(figsize=(12,7))
    sns.countplot(data=df, x='Age', palette='viridis')
    plt.show()

# Câu 3: Thống kê số lượng người dùng theo nghề nghiệp (Occupation). Nghề nào chiếm đa số?
def cau_3():
    Occupation_count = df['Occupation'].value_counts().sort_values(ascending=False)
    print(Occupation_count)
    print('KẾT LUẬN: thống kê số lượng người theo nghề nghiệp cho thấy k có chênh lệch quá lớn giữa các nghề nghiệp làm cho dữ liệu khách quan hơn.')

# Câu 4: So sánh tỷ lệ sử dụng thiết bị Android và iOS qua biểu đồ tròn (Pie Chart).
def cau_4():
    data = df['Device_Type'].value_counts()
    plt.figure(figsize=(12,7))
    categories = ['IOS', 'Android']
    plt.pie(data, labels=categories, autopct='%1.1f%%' )
    plt.show()

# --- NHÓM 2: THÓI QUEN SỬ DỤNG SMARTPHONE (CÂU 5 - 8) ---
# Câu 5: Tính trung bình số giờ sử dụng điện thoại (Daily_Phone_Hours) của từng nhóm nghề nghiệp.
def cau_5():
    Daily_Phone_Hours = df.groupby('Occupation')['Daily_Phone_Hours'].mean()
    print(Daily_Phone_Hours)

# Câu 6: Vẽ biểu đồ Scatter Plot thể hiện mối quan hệ giữa "Tổng giờ dùng điện thoại" và "Giờ dùng mạng xã hội".
# TỐI ƯU CHO 50.000 DÒNG:
    # 1. Thêm alpha=0.1 để các chấm mờ đi, chỗ nào đậm là mật độ cao.
    # 2. Thêm hue='Device_Type' để so sánh Android/iOS.
    # 3. Dùng s=10 để thu nhỏ kích thước chấm.
def cau_6():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Daily_Phone_Hours', y='Social_Media_Hours', 
                    hue='Device_Type', alpha=0.1, s=10, palette='deep')
    
    plt.title('Quan hệ giữa Tổng giờ dùng điện thoại và Giờ dùng Mạng xã hội', fontsize=14)
    plt.xlabel('Tổng giờ dùng điện thoại (h)')
    plt.ylabel('Giờ dùng Mạng xã hội (h)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Câu 7: Người dùng Android hay iOS có xu hướng cài đặt nhiều ứng dụng (App_Usage_Count) hơn?
def cau_7():
    user_trend = df.groupby('Device_Type')['App_Usage_Count'].sum()
    print(user_trend)
    plt.figure(figsize=(12,7))
    plt.title('Câu 7: Người dùng Android hay iOS có xu hướng cài đặt nhiều ứng dụng (App_Usage_Count) hơn?')
    plt.xlabel('Device_Type')
    plt.ylabel('App_Usage_Count')
    sns.countplot(data=df, x='Device_Type', palette='viridis')
    plt.show()
    print('KẾT LUẬN: số lượng app giữa người sử dụng android và IOS k có sự khác biệt quá nhiều')

# Câu 8: So sánh thời gian dùng điện thoại giữa Ngày thường (Daily) và Cuối tuần (Weekend_Screen_Time).
def cau_8():
    print("\n--- CÂU 8: NGÀY THƯỜNG VS CUỐI TUẦN ---")
    avg_daily = df['Daily_Phone_Hours'].mean()
    avg_weekend = df['Weekend_Screen_Time_Hours'].mean()
    
    plt.figure(figsize=(8, 5))
    plt.bar(['Ngày thường', 'Cuối tuần'], [avg_daily, avg_weekend], color=['red', 'blue'])
    plt.title('So sánh thời gian sử dụng: Ngày thường vs Cuối tuần')
    plt.ylabel('Số giờ trung bình')
    plt.show()
    print('KẾT LUẬN: số giờ sử dụng điện thoại vào cuối tuần cao hơn số giờ sử dụng trong ngày thường cao hơn khá nhiều')

# --- NHÓM 3: SỨC KHỎE & LỐI SỐNG (CÂU 9 - 11) ---
# Câu 9: Vẽ biểu đồ tương quan giữa "Số giờ dùng mạng xã hội" và "Số giờ ngủ". Có phải dùng nhiều thì ngủ ít?
def cau_9():
    data = df[['Social_Media_Hours', 'Sleep_Hours']]
    plt.figure(figsize=(12, 7))
    df_sample = df.sample(5000)
    sns.regplot(data=df_sample, x='Social_Media_Hours', y='Sleep_Hours', 
                scatter_kws={'alpha':0.2, 's':15}, line_kws={'color':'red'})
    
    plt.title('Mối quan hệ giữa Giờ dùng Mạng xã hội và Số giờ ngủ', fontsize=14)
    plt.xlabel('Giờ mạng xã hội')
    plt.ylabel('Số giờ ngủ')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    print('KẾT LUẬN: số giờ ngủ nhiều hay ít k liên quan đến việc sử dụng mạng xã hội bởi vì theo như biểu đồ thì nó là 1 đường ngang tức x = 0 nên số giờ sử dụng mạng hội k ảnh hưởng')

# Câu 10: Phân tích mức độ căng thẳng (Stress_Level) trung bình theo lượng Caffeine tiêu thụ.
def cau_10():
    stress_level = df.groupby('Caffeine_Intake_Cups')['Stress_Level'].mean()
    print(stress_level)
    print('KẾT LUẬN: theo như dữ liệu thì lượng cà phê tiêu thụ k ảnh hưởng quá lớn đến mức độ Stress')

# Câu 11: Tìm mối quan hệ giữa Stress_Level và Sleep_Hours qua biểu đồ nhiệt (Heatmap) hoặc Scatter.
def cau_11():
    print("\n--- CÂU 11: MỐI QUAN HỆ GIỮA STRESS VÀ GIẤC NGỦ ---")
    plt.figure(figsize=(12, 7))
    # Lấy mẫu 2000 dòng để vẽ cho rõ
    df_sample = df.sample(2000)
    sns.regplot(data=df_sample, x='Stress_Level', y='Sleep_Hours', 
                scatter_kws={'alpha':0.3, 's':20, 'color': 'teal'}, 
                line_kws={'color':'red', 'label': 'Xu hướng chung'})
    
    plt.title('Phân tích nghịch biến: Stress Level vs Sleep Hours', fontsize=14)
    plt.xlabel('Mức độ Stress (1-10)')
    plt.ylabel('Số giờ ngủ (h)')
    plt.legend()
    plt.show()

# --- NHÓM 4: HIỆU SUẤT CÔNG VIỆC & TƯƠNG QUAN TỔNG THỂ (CÂU 12 - 15) ---
# Câu 12: Vẽ biểu đồ thể hiện điểm năng suất (Work_Productivity_Score) trung bình theo từng nhóm tuổi.
def cau_12():
    age_Work_Productivity = df.groupby('Age')['Work_Productivity_Score'].mean()
    print(age_Work_Productivity)
    print('KẾT LUẬN: độ tuổi k ảnh hưởng đến năng suất làm việc quá nhiều')

# Câu 13: Những người có năng suất công việc cao (Score > 8) thường có thói quen dùng điện thoại như thế nào?
def cau_13():
    print("\n--- CÂU 13: PHÂN TÍCH XU HƯỚNG NHÓM NĂNG SUẤT CAO (SCORE > 8) ---")
    
    # Bước 1: Lọc nhóm năng suất cao
    high_prod_df = df[df['Work_Productivity_Score'] > 8]
    
    # Bước 2: Tạo Pivot Table hợp lý
    # Tao chọn index='Occupation' (Nghề nghiệp) và columns='Device_Type' (Thiết bị)
    # values='Social_Media_Hours' để xem nhóm "Pro" này dùng mạng xã hội bao nhiêu
    summary = high_prod_df.pivot_table(
        values='Social_Media_Hours', 
        index='Occupation', 
        columns='Device_Type', 
        aggfunc='mean', 
        fill_value=0
    )
    
    print("Bảng thống kê giờ dùng Mạng xã hội trung bình của nhóm Năng suất cao:")
    print(summary)
    
    # Bước 3: Vẽ Heatmap từ Pivot Table này để nhìn xu hướng cho nhanh
    plt.figure(figsize=(10, 6))
    sns.heatmap(summary, annot=True, cmap='YlOrRd', fmt=".2f")
    plt.title('Giờ dùng MXH trung bình của nhóm Năng suất cao theo Nghề nghiệp')
    plt.show()

# Câu 14: Vẽ ma trận tương quan (Heatmap) cho tất cả các biến số để tìm ra những cặp yếu tố ảnh hưởng mạnh nhất.
def cau_14():
    plt.figure(figsize=(12,7))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr,annot=True, cmap='coolwarm', fmt=".2f" )
    plt.show()

# Câu 15: Dự đoán (giả định): Nếu giảm 2 giờ dùng mạng xã hội, Stress_Level trung bình của sinh viên (Student) thay đổi ra sao?
def cau_15():
    print("\n--- CÂU 15: GIẢ ĐỊNH GIẢM 2 GIỜ MẠNG XÃ HỘI CHO SINH VIÊN ---")
    
    # Bước 1: Lọc riêng nhóm Sinh viên
    students = df[df['Occupation'] == 'Student'].copy()
    
    # Bước 2: Tính toán các chỉ số thống kê cần thiết
    avg_social = students['Social_Media_Hours'].mean()
    avg_stress = students['Stress_Level'].mean()
                                       
    # Tính hệ số tương quan (r)
    r = students['Social_Media_Hours'].corr(students['Stress_Level'])
    
    # Tính độ lệch chuẩn (std) để tìm "tốc độ thay đổi" (Slope)
    std_stress = students['Stress_Level'].std()
    std_social = students['Social_Media_Hours'].std()
    
    # Hệ số hồi quy (m) - Cho biết giảm 1 giờ MXH thì Stress giảm bao nhiêu đơn vị
    slope = r * (std_stress / std_social)
    
    # Bước 3: Thực hiện giả định giảm 2 giờ
    reduction = 2
    estimated_stress_reduction = slope * reduction
    new_avg_stress = avg_stress - estimated_stress_reduction
    
    # Bước 4: In kết quả
    print(f"Số lượng sinh viên phân tích: {len(students)}")
    print(f"Mức Stress trung bình hiện tại: {avg_stress:.2f}")
    print(f"Hệ số tác động (Slope): {slope:.4f}")
    
    print("-" * 30)
    print(f"KỊCH BẢN: Nếu mỗi sinh viên giảm {reduction} giờ dùng Mạng xã hội/ngày:")
    print(f"=> Mức Stress dự kiến sẽ giảm: {estimated_stress_reduction:.2f} đơn vị.")
    print(f"=> Mức Stress trung bình mới sẽ là: {new_avg_stress:.2f}")
    print("-" * 30)

    # Vẽ biểu đồ minh họa sự thay đổi
    plt.figure(figsize=(8, 6))
    plt.bar(['Hiện tại', 'Sau khi giảm 2h MXH'], [avg_stress, new_avg_stress], color=['grey', 'green'])
    plt.title('Dự báo thay đổi Mức độ Stress của Sinh viên', fontsize=14)
    plt.ylabel('Mức độ Stress (1-10)')
    plt.ylim(0, 10) # Để thang đo từ 0-10 cho dễ so sánh
    plt.show()
