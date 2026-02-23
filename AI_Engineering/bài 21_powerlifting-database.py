import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
# --- 1. TRIỆU HỒI DỮ LIỆU ---
try:
    df = pd.read_csv('meets.csv')
    print("--- ĐÃ TẢI DỮ LIỆU MEETS THÀNH CÔNG ---")
except:
    print("--- LỖI: KHÔNG TÌM THẤY FILE meets.csv ---")

# =========================================================================
# THUẬT NGỮ CỐT LÕI (GLOSSARY)
# =========================================================================
# Meet:           Một cuộc thi/giải đấu Powerlifting cụ thể.
# Federation:     Liên đoàn tổ chức (Ví dụ: IPF, USAPL, 365Strong). Mỗi liên đoàn có luật riêng.
# MeetCountry:    Quốc gia diễn ra giải đấu.
# MeetState/Town: Bang và Thành phố diễn ra giải đấu.
# MeetPath:       Đường dẫn định danh duy nhất của giải đấu trong hệ thống OpenPowerlifting.
# =========================================================================

# =========================================================================
# KHUNG SƯỜN 15 NHIỆM VỤ (LEVEL: DATA STRATEGIST)
# =========================================================================

# --- NHÓM 1: KHÁM PHÁ & LÀM SẠCH (CÂU 1 - 4) ---
# Câu 1: Kiểm tra kích thước dữ liệu và xem 5 dòng đầu tiên.
def cau_1():
    print("\n--- CÂU 1: KIỂM TRA TỔNG QUAN ---")
    print(f"Số dòng: {df.shape[0]}, Số cột: {df.shape[1]}")
    print('5 hàng đầu của dữ liệu: \n',df.head(5) )

# Câu 2: Đếm số lượng giá trị thiếu (NaN) ở các cột MeetState và MeetTown.
def cau_2():
    print('số lượng giá trị thiếu (NaN)')
    print(df.isnull().sum())

# Câu 3: Chuyển đổi cột 'Date' sang kiểu dữ liệu datetime.
df['Date'] = pd.to_datetime(df['Date'])


# Câu 4: Trích xuất 'Year' và 'Month' từ cột Date để phục vụ phân tích thời gian.

df['Years'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month


# --- NHÓM 2: PHÂN TÍCH QUY MÔ (CÂU 5 - 8) ---
# Câu 5: Có tổng cộng bao nhiêu Liên đoàn (Federation) khác nhau trong dữ liệu?
def cau_5():
    print('Câu 5: Có tổng cộng bao nhiêu Liên đoàn (Federation) khác nhau trong dữ liệu?')
    res = df['Federation'].drop_duplicates()
    print('có',res.count(), 'liên đoàn khác nhau trong dữ liệu')

# Câu 6: Top 10 Quốc gia tổ chức nhiều giải đấu nhất là những nước nào? Vẽ biểu đồ cột.
def cau_6():
    print('Câu 6: Top 10 Quốc gia tổ chức nhiều giải đấu nhất là những nước nào?')
    top_10_country = df['MeetCountry'].value_counts().head(10)
    print(top_10_country)

    plt.figure(figsize=(12, 6))
    # Dùng sns.barplot: x là tên nước (index), y là số lượng (values)
    sns.barplot(x=top_10_country.index, y=top_10_country.values, palette='magma')
    plt.title('Top 10 Quốc gia tổ chức nhiều giải đấu Powerlifting nhất', fontsize=14)
    plt.xlabel('Quốc gia')
    plt.ylabel('Số lượng giải đấu')
    plt.xticks(rotation=45) # Xoay tên nước cho dễ đọc
    plt.tight_layout()
    plt.show()

# Câu 7: Liên đoàn nào hoạt động năng nổ nhất (tổ chức nhiều giải nhất)?
def cau_7():
    print('Câu 7: Liên đoàn nào hoạt động năng nổ nhất (tổ chức nhiều giải nhất)?')
    top_Federation = df['Federation'].value_counts().head(1)
    print('liên đoàn hoạt động năng nổ nhất là: \n',top_Federation )

# Câu 8: Tính tỷ lệ % số giải đấu được tổ chức tại 'USA' so với phần còn lại của thế giới.
def cau_8():
    print("\n--- CÂU 8: TỶ LỆ GIẢI ĐẤU TẠI USA ---")
    # LƯU Ý:
    # Đừng dùng .count() vì nó trả về Series cho mọi cột.
    # Dùng len() trên dataframe đã lọc để lấy 1 con số duy nhất (số lượng hàng).
    usa_meets = df[df['MeetCountry'] == 'USA']
    usa_count = len(usa_meets) 
    total_count = len(df)
    percentage = (usa_count / total_count) * 100
    print(f"Số lượng giải đấu tại USA: {usa_count}")
    print(f"Tỷ lệ giải đấu tổ chức tại USA: {percentage:.2f}%")

# --- NHÓM 3: XU HƯỚNG THỜI GIAN (CÂU 9 - 11) ---
# Câu 9: Vẽ biểu đồ đường thể hiện số lượng giải đấu thay đổi qua các năm.
def cau_9():
    
    year_counts = df['Years'].value_counts().sort_index()
    # Bước 2: Vẽ biểu đồ đường
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o', color='crimson', linewidth=2)
    plt.title('Sự tăng trưởng số lượng giải đấu Powerlifting qua các năm', fontsize=14)
    plt.xlabel('Năm')
    plt.ylabel('Số lượng giải đấu')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Câu 10: Các giải đấu thường tập trung vào tháng mấy trong năm? (Phân tích tính mùa vụ).
def cau_10():
    print("\n--- CÂU 10: PHÂN BỔ GIẢI ĐẤU THEO THÁNG (ALL YEARS) ---")
    # Bước 1: Gom nhóm theo tháng và đếm số lượng giải
    # Cách này giúp mày so sánh các tháng cực kỳ dễ dàng vì nó cộng dồn tất cả các năm
    month_counts = df['Month'].value_counts().sort_index()
    # Bước 2: Vẽ biểu đồ cột
    plt.figure(figsize=(10, 6))
    colors = sns.color_palette('Blues_d', n_colors=12) # Tạo dải màu xanh
    sns.barplot(x=month_counts.index, y=month_counts.values, palette=colors)
    plt.title('Tổng số lượng giải đấu Powerlifting theo tháng (Toàn bộ dữ liệu)', fontsize=14)
    plt.xlabel('Tháng trong năm', fontsize=12)
    plt.ylabel('Số lượng giải đấu', fontsize=12)
    plt.xticks(range(0, 12), ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'])
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

# Câu 11: Tạo cột 'Weekday' (Thứ trong tuần). Các giải đấu thường diễn ra vào Thứ Bảy/Chủ Nhật hay ngày thường?
def cau_11():   
    df['Weekday'] = df['Date'].dt.weekday
    df['Day_Type'] = np.where(df['Weekday'] >= 5, 'Weekend (T7-CN)', 'Weekday (T2-T6)')
    
    # Thống kê
    stats = df['Day_Type'].value_counts()
    print("Kết quả thống kê:")
    print(stats)
    
    # Tính phần trăm
    percent = df['Day_Type'].value_counts(normalize=True) * 100
    print("\nTỷ lệ phần trăm:")
    print(percent)

    # Vẽ biểu đồ cột để so sánh trực quan
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Day_Type', palette='Set1')
    plt.title('So sánh số lượng giải đấu: Cuối tuần vs Ngày thường')
    plt.ylabel('Số lượng giải')
    plt.show()

# --- NHÓM 4: PHÂN TÍCH SÂU & THỊ GIÁC HÓA (CÂU 12 - 15) ---
# Câu 12: Tại USA, Top 5 bang (MeetState) nào là "thủ phủ" của Powerlifting?
def cau_12():
    usa_data = df[df['MeetCountry'] == 'USA']
    state_counts = usa_data['MeetState'].value_counts().head(5)
    print("top 5 bang là thủ phủ của USA là: \n", state_counts)

# Câu 13: Vẽ biểu đồ Heatmap thể hiện số lượng giải đấu (Trục X: Tháng, Trục Y: Năm).
def cau_13():
    df_recent = df[df['Years'] >= 2010]
    
    # Bước 3: Tạo Pivot Table - Trái tim của Heatmap
    # index (hàng) là Tháng, columns (cột) là Năm
    pivot_data = df_recent.pivot_table(
        values='MeetID', 
        index='Month', 
        columns='Years', 
        aggfunc='count', 
        fill_value=0
    )
    
    # Bước 4: Vẽ Heatmap
    plt.figure(figsize=(15, 8))
    # annot=True để hiện số, fmt="d" để định dạng số nguyên, cmap là bảng màu
    sns.heatmap(pivot_data, annot=True, fmt="d", cmap="coolwarm", linewidths=.5)
    
    plt.title('Bản đồ nhiệt: Mật độ giải đấu Powerlifting (Tháng vs Năm)', fontsize=16)
    plt.xlabel('Năm phát hành', fontsize=12)
    plt.ylabel('Tháng trong năm', fontsize=12)
    
    # Tùy chỉnh nhãn trục Y cho dễ đọc (thay vì 1, 2, 3...)
    plt.yticks(np.arange(0.5, 12.5), ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'], rotation=0)
    
    plt.show()

# Câu 14: Lọc ra các giải đấu của liên đoàn 'IPF'. Xem xu hướng tổ chức của riêng liên đoàn này.
def cau_14():
    IPF_Federation = df[df['Federation'] == 'IPF']
    pivot_data = IPF_Federation.pivot_table(
        values='MeetID', 
        index='Month', 
        columns='Years', 
        aggfunc='count', 
        fill_value=0
    )
    plt.figure(figsize=(12,7))
    sns.heatmap(pivot_data, cmap = 'coolwarm', annot=True, fmt='d', linewidths=.5)
    plt.show()


# Câu 15: Tìm 5 thành phố (MeetTown) tổ chức nhiều giải đấu nhất thế giới.
def cau_15():
    top_5_MeetTown = df['MeetTown'].value_counts().head(5)
    print(top_5_MeetTown)




