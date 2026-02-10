import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. TRIỆU HỒI DỮ LIỆU ---
# Sử dụng file boston.csv mày đã upload
try:
    df = pd.read_csv('boston.csv')
    print("--- ĐÃ TẢI DỮ LIỆU BOSTON HOUSING THÀNH CÔNG ---")
except:
    print("--- LỖI: KHÔNG TÌM THẤY FILE boston.csv ---")

# =========================================================================
# TỪ ĐIỂN DỮ LIỆU (DỊCH CHO MÀY DỄ HÌNH DUNG)
# =========================================================================
# CRIM:     Tỷ lệ tội phạm bình quân đầu người theo thị trấn
# ZN:       Tỷ lệ đất ở được quy hoạch cho các lô trên 25.000 sq.ft.
# INDUS:    Tỷ lệ diện tích kinh doanh phi bán lẻ trên mỗi thị trấn
# CHAS:     Biến giả sông Charles (= 1 nếu giáp sông; 0 nếu không)
# NOX:      Nồng độ oxit nitơ (phần trên 10 triệu)
# RM:       Số phòng trung bình trên mỗi căn hộ (CỰC KỲ QUAN TRỌNG)
# AGE:      Tỷ lệ các căn hộ do chủ sở hữu chiếm hữu được xây dựng trước năm 1940
# DIS:      Khoảng cách có trọng số đến 5 trung tâm việc làm ở Boston
# RAD:      Chỉ số khả năng tiếp cận đường cao tốc hướng tâm
# TAX:      Thuế suất thuế tài sản toàn giá trị trên $10,000
# PTRATIO:  Tỷ lệ học sinh-giáo viên theo thị trấn
# B:        1000(Bk - 0.63)^2 trong đó Bk là tỷ lệ người da đen theo thị trấn
# LSTAT:    Tỷ lệ dân số có địa vị thấp (%)
# MEDV:     Giá trị trung bình của những ngôi nhà do chủ sở hữu chiếm hữu tính theo $1000s (MỤC TIÊU)
# =========================================================================
print("-" * 50)

# =========================================================================
# BÀI TẬP THỬ THÁCH (LEVEL: INTERMEDIATE)
# =========================================================================

# Câu 1: Kiểm tra xem dữ liệu có giá trị thiếu (NaN) nào không? 
# Nếu không có, hãy thử dùng hàm describe() để xem thống kê tổng quát.
def cau_1():
    print(df.isnull().sum())
    print("dữ liệu k có giá trị NaN")
    print(df.describe())


# Câu 2: Tìm cột có tương quan (Correlation) mạnh nhất với giá nhà (MEDV).
# Gợi ý: Dùng df.corr()['MEDV'].sort_values()
def cau_2():
    corr = df.corr()['MEDV'].sort_values(ascending=False)
    print(corr)


# Câu 3: Vẽ biểu đồ phân tán (Scatter Plot) giữa cột 'RM' (Số phòng) và 'MEDV' (Giá nhà).
# Nhận xét xem số phòng càng nhiều thì giá nhà có càng cao không?
def cau_3():
    plt.figure(figsize=(10, 6))
    # Dùng regplot thay vì scatterplot để vẽ thêm đường xu hướng (màu đỏ)
    # scatter_kws={'alpha':0.5}: giúp các điểm mờ đi, chỗ nào đậm là chỗ đó tập trung nhiều dữ liệu
    sns.regplot(data=df, x='RM', y='MEDV', 
                scatter_kws={'alpha':0.5, 'color':'teal'}, 
                line_kws={'color':'red'})
    
    plt.title('Quan hệ giữa Số phòng (RM) và Giá nhà (MEDV)', fontsize=14)
    plt.xlabel('Số phòng trung bình (RM)', fontsize=12)
    plt.ylabel('Giá nhà trung bình (MEDV - $1000s)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Câu 4: Lọc ra những khu vực có "Tỷ lệ tội phạm" (CRIM) thấp hơn mức trung bình 
# nhưng lại có "Giá nhà" (MEDV) cao hơn mức trung bình.
def cau_4():
    low_prime_area = df[(df['CRIM'] < df['CRIM'].mean()) & (df['MEDV'] > df['MEDV'].mean())] 
    print(low_prime_area)
    count = len(low_prime_area)
    total = len(df)
    percentage = (count / total) * 100
    print("\n--- CÂU 4: KHU VỰC TỘI PHẠM THẤP & GIÁ NHÀ CAO ---")
    print(f"Số lượng khu vực thỏa mãn: {count} trên tổng số {total}")
    print(f"Tỷ lệ chiếm: {percentage:.2f}%")

# Câu 5: Tạo cột mới 'TAX_Rate' = TAX / 100. Sau đó phân loại khu vực có 
# mức thuế cao (High) và thấp (Low) dựa trên trung vị (median) của cột này.

def cau_5():
    df['TAX_Rate'] = df['TAX'] / 100
    tax_median = df['TAX_Rate'].median()
    df['TAX_Level'] = np.where(df['TAX_Rate'] > tax_median, 'High', 'Low')
    print(df)


# Câu 6: Vẽ biểu đồ Heatmap để xem toàn cảnh sự tương quan giữa các yếu tố.
def cau_6():
    plt.figure(figsize=(8, 6))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('biểu đồ Heatmap để xem toàn cảnh sự tương quan giữa các yếu tố')
    plt.show()

# Câu 7: Tìm 5 khu vực có tỷ lệ dân số thu nhập thấp (LSTAT) cao nhất. 
# Xem thử giá nhà ở đó như thế nào?
def cau_7():
    top_5_LSTAT = df.sort_values(by='LSTAT', ascending=False).head(5)
    top_5_LSTAT_price = top_5_LSTAT[['LSTAT', 'MEDV', 'CRIM', 'RM']]
    print(top_5_LSTAT_price)
    print('nhận xét: các khu vực có LSTAT cao nhất thì có giá tiền (MEDV) thấp hơn mức trung bình. ngược lại tỉ lệ tội phạm lại cao 1 cách bất thường')

# Câu 8: Sử dụng Boxplot để so sánh giá nhà (MEDV) giữa khu vực giáp sông (CHAS=1) 
# và không giáp sông (CHAS=0). Ở đâu nhà đắt hơn?
def cau_8():
    plt.figure(figsize=(10, 6))
    plot_data = df.copy()
    plot_data['CHAS_Label'] = plot_data['CHAS'].map({0: 'Không giáp sông', 1: 'Giáp sông'})
    
    # Vẽ Boxplot: x là biến phân loại, y là biến số (Giá nhà)
    sns.boxplot(data=plot_data, x='CHAS_Label', y='MEDV', palette='Set2', width=0.5)
    
    # Thêm Stripplot (các điểm chấm) để thấy rõ mật độ phân bổ dữ liệu
    sns.stripplot(data=plot_data, x='CHAS_Label', y='MEDV', color="black", alpha=0.3)
    
    plt.title('Sự khác biệt giá nhà dựa trên vị trí giáp sông Charles', fontsize=14)
    plt.xlabel('Vị trí khu vực', fontsize=12)
    plt.ylabel('Giá nhà trung bình ($1000s)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Câu 9: Tính giá nhà trung bình cho mỗi mức chỉ số tiếp cận đường cao tốc (RAD).
def cau_9():
    RAD_group = df.groupby('RAD')['MEDV'].mean().sort_values(ascending=False)
    print(RAD_group)

# Câu 10 (CÂU CHỐT): Vẽ biểu đồ phân phối (Distribution Plot) của giá nhà (MEDV).
# Nó có bị lệch (skew) về bên nào không?
def cau_10():
    plt.figure(figsize=(10, 6))
    
    # Vẽ Histogram kèm đường KDE để xem độ lệch
    sns.histplot(data=df, x='MEDV', kde=True, color='blue', bins=30)
    
    plt.title('Phân phối giá nhà trung bình tại Boston', fontsize=14)
    plt.xlabel('Giá nhà (MEDV - $1000s)', fontsize=12)
    plt.ylabel('Tần suất (Count)', fontsize=12)
    
    # Tính toán độ lệch (Skewness) để trả lời câu hỏi phụ
    skewness = df['MEDV'].skew()
    print(f"\n--- CÂU 10: PHÂN PHỐI GIÁ NHÀ ---")
    print(f"Độ lệch (Skewness) của giá nhà: {skewness:.2f}")
    
    if skewness > 0:
        print("Kết luận: Biểu đồ bị lệch phải (Positive Skew).")
    else:
        print("Kết luận: Biểu đồ bị lệch trái (Negative Skew).")
    plt.show()
print("\n--- CHÀO MỪNG MÀY ĐẾN VỚI THẾ GIỚI HỒI QUY ---")

if __name__ == "__main__":
    cau_1()
    cau_2()
    cau_3()
    cau_4()
    cau_5()
    cau_6()
    cau_7()
    cau_8()
    cau_9()
    cau_10()