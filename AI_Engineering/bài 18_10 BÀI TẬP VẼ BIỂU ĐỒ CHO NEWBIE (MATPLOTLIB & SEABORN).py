import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# =========================================================================
# 0. KHỞI TẠO DỮ LIỆU DÙNG CHUNG
# =========================================================================
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp = [28, 30, 25, 32, 35, 31, 29]
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 15, 40]

np.random.seed(42)
data = pd.DataFrame({
    'Total_Bill': np.random.uniform(10, 100, 100),
    'Tip': np.random.uniform(2, 20, 100),
    'Day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 100),
    'Size': np.random.randint(1, 6, 100)
})

# =========================================================================
# PHẦN 1: MATPLOTLIB (VẼ CƠ BẢN)
# =========================================================================

def bai_1():
    """Biểu đồ đường cơ bản"""
    plt.figure(figsize=(8, 4))
    plt.plot(days, temp)
    plt.title('Bài 1: Nhiệt độ trong tuần')
    plt.xlabel('Thứ')
    plt.ylabel('Nhiệt độ (C)')
    plt.show()

def bai_2():
    """Tùy chỉnh phong cách (Màu đỏ, nét đứt, marker)"""
    plt.figure(figsize=(8, 4))
    plt.plot(days, temp, color='red', linestyle='--', marker='o', linewidth=2)
    plt.title('Bài 2: Nhiệt độ tùy chỉnh phong cách')
    plt.grid(True)
    plt.show()

def bai_3():
    """Biểu đồ cột đa màu sắc"""
    plt.figure(figsize=(8, 4))
    plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
    plt.title('Bài 3: Biểu đồ cột danh mục')
    plt.xlabel('Danh mục')
    plt.ylabel('Giá trị')
    plt.show()

def bai_4():
    """Biểu đồ tròn hiển thị %"""
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Bài 4: Tỷ lệ phần trăm các danh mục')
    plt.show()

# =========================================================================
# PHẦN 2: SEABORN (VẼ CHUYÊN NGHIỆP)
# =========================================================================

def bai_5():
    """Biểu đồ phân tán phân loại theo màu (hue)"""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Total_Bill', y='Tip', hue='Day', size='Size', palette='deep')
    plt.title('Bài 5: Mối quan hệ giữa Hóa đơn và Tiền Tip')
    plt.show()

def bai_6():
    """Biểu đồ tần suất (Histogram & KDE)"""
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='Total_Bill', kde=True, color='purple', bins=20)
    plt.title('Bài 6: Phân phối tổng hóa đơn')
    plt.show()

def bai_7():
    """Biểu đồ hộp tìm Outliers"""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='Day', y='Total_Bill', palette='Set2')
    plt.title('Bài 7: Biến động hóa đơn theo từng ngày')
    plt.show()

def bai_8():
    """Biểu đồ đếm số lượng"""
    plt.figure(figsize=(8, 5))
    sns.countplot(data=data, x='Day', palette='viridis')
    plt.title('Bài 8: Số lượng hóa đơn mỗi ngày')
    plt.show()

def bai_9():
    """Ma trận tương quan (Heatmap)"""
    
    plt.figure(figsize=(8, 6))
    corr = data.select_dtypes(include=[np.number]).corr()
    
    # annot=True: Hiện số lên ô
    # cmap='coolwarm': Màu đỏ (thuận), xanh (nghịch)
    # fmt=".2f": Lấy 2 chữ số thập phân
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Bài 9: Ma trận tương quan các biến số')
    plt.show()

def bai_10():
    """Biểu đồ cặp - Nhìn tổng quan"""
    print("Đang vẽ Bài 10... (Vui lòng đợi)")
    pair_plot = sns.pairplot(data, hue='Day', palette='husl')
    pair_plot.fig.suptitle('Bài 10: Tổng quan mối quan hệ giữa các biến', y=1.02)
    plt.show()

# =========================================================================
# KHU VỰC CHẠY THỬ 
# =========================================================================
if __name__ == "__main__":
    bai_5()
