import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. TRIỆU HỒI DỮ LIỆU ---
try:
    df = pd.read_csv('tmdb_movies.csv')
    print("--- ĐÃ TẢI DỮ LIỆU TMDB MOVIES THÀNH CÔNG ---")
except:
    print("--- LỖI: KHÔNG TÌM THẤY FILE tmdb_movies.csv ---")

# =========================================================================
# TỪ ĐIỂN DỮ LIỆU
# =========================================================================
# title:              Tên phim
# genre:              Thể loại (có thể chứa nhiều thể loại cách nhau bởi dấu phẩy)
# release_year:       Năm phát hành
# budget:             Kinh phí sản xuất ($)
# revenue:            Doanh thu ($)
# runtime:            Thời lượng phim (phút)
# vote_average:       Điểm đánh giá trung bình
# vote_count:         Số lượng người đánh giá
# production_country: Quốc gia sản xuất
# =========================================================================

# =========================================================================
# BÀI TẬP THỬ THÁCH (LEVEL: DATA NINJA)
# =========================================================================

# Câu 1: Kiểm tra tổng quan dữ liệu. 
# Có bao nhiêu dòng, bao nhiêu cột? Có dữ liệu nào bị thiếu không?
def cau_1():
    print(df.describe())
    print(df.isnull().sum())
    print("kết luận: dữ liệu đầy đủ")

# Câu 2: Tạo thêm 2 cột mới cực kỳ quan trọng:
# - 'profit': Doanh thu trừ kinh phí (Revenue - Budget).
# - 'ROI': Tỷ suất hoàn vốn (Revenue / Budget). Nếu Budget = 0, hãy để ROI = 0.

df['profit'] = df['revenue'] - df['budget']
try:
    df['ROI'] = df['revenue'] / df['budget']
except ZeroDivisionError:
    df['ROI'] = 0


# Câu 3: Tìm 10 bộ phim có "Lợi nhuận" (profit) cao nhất mọi thời đại. 
# Vẽ biểu đồ cột để so sánh 10 phim này.
def cau_3():
    unique_movies = df.drop_duplicates(subset='title')
    
    # Bước 2: Lấy top 10
    top_10_profit = unique_movies.sort_values(by='profit', ascending=False).head(10)
    
    plt.figure(figsize=(12, 6))
    # Dùng seaborn barplot để màu sắc tự động và đẹp hơn
    sns.barplot(data=top_10_profit, x='title', y='profit', palette='viridis')
    
    plt.title('Top 10 bộ phim có lợi nhuận cao nhất mọi thời đại', fontsize=14)
    plt.xlabel('Tên phim', fontsize=12)
    plt.ylabel('Lợi nhuận ($)', fontsize=12)
    
    # Bước 3: Xoay nhãn trục X để không bị chồng lấn (trùng chữ)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Tự động căn chỉnh để không mất chữ
    plt.show()

# Câu 4: Cột 'genre' chứa chuỗi các thể loại (ví dụ: "Action, Comedy").
print("\n--- CÂU 4: TRÍCH XUẤT THỂ LOẠI CHÍNH ---")
df['main_genre'] = df['genre'].str.split(',').str[0]
    


# Câu 5: Doanh thu điện ảnh thay đổi thế nào qua các năm?
# Hãy vẽ biểu đồ đường (Line Plot) thể hiện Tổng doanh thu theo 'release_year'.
def cau_5():
    # Bước 1: Gộp nhóm để tính TỔNG doanh thu theo năm (Dùng line plot trên dữ liệu thô sẽ ra vùng mờ CI rất rối)
    yearly_data = df.groupby('release_year')['revenue'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=yearly_data, x='release_year', y='revenue', 
                 marker='o', markersize=8, color="#0082e0", linewidth=2.5, label='Tổng doanh thu')
    plt.title('Xu Hướng Tổng Doanh Thu Điện Ảnh Qua Các Năm', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Năm Phát Hành', fontsize=12)
    plt.ylabel('Tổng Doanh Thu ($)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()



# Câu 6: Có phải phim càng dài (runtime) thì điểm càng cao (vote_average) không?
# Vẽ biểu đồ phân tán (Scatter Plot) để kiểm tra giả thuyết này.
def cau_6():
    print("\n--- CÂU 6: QUAN HỆ GIỮA THỜI LƯỢNG VÀ ĐIỂM SỐ ---")
    plt.figure(figsize=(10, 6))
    
    # Dùng sns.regplot để vẽ cả điểm phân tán và đường hồi quy thẳng qua vùng mật độ cao
    # x='vote_average': Điểm trung bình, y='runtime': Thời lượng phim
    sns.regplot(data=df, x='vote_average', y='runtime', 
                scatter_kws={'alpha': 0.3, 'color': 'teal'}, 
                line_kws={'color': 'red', 'label': 'Đường xu hướng'})
    
    plt.xlabel('Điểm đánh giá trung bình (Score)', fontsize=12)
    plt.ylabel('Thời lượng phim (phút)', fontsize=12)
    plt.title('Biểu đồ phân tán & Đường xu hướng giữa Điểm số và Thời lượng', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# Câu 7: Thống kê số lượng phim được sản xuất bởi mỗi quốc gia (production_country).
# Lấy Top 5 quốc gia sản xuất nhiều phim nhất.
def cau_7():
    print("\n--- CÂU 7: QUỐC GIA SẢN XUẤT PHIM NHIỀU NHẤT ---")
    film_of_nation = (df.groupby('production_country')['title'].count().sort_values(ascending=False))
    print('các quốc gia có số lượng phim từ cao đến thấp là: \n', film_of_nation)

# Câu 8: Sử dụng Boxplot để so sánh điểm số (vote_average) giữa các năm phát hành (release_year).
# (Chỉ lấy dữ liệu từ năm 2000 trở lại đây cho dễ nhìn).
def cau_8():
    print("\n--- CÂU 8: BIẾN ĐỘNG ĐIỂM SỐ THEO NĂM (TỪ 2000) ---")
    recent_df = df[df['release_year'] >= 2000]
    plt.figure(figsize=(15, 7))
    sns.boxplot(data=recent_df, x='release_year', y='vote_average', palette='coolwarm')
    plt.title('Phân bổ điểm đánh giá qua các năm (2000 - Nay)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle ='--', alpha=0.6)
    plt.show()

# Câu 9: Tìm mối tương quan giữa 'budget', 'revenue', 'runtime', và 'vote_count'.
# Vẽ Heatmap để thể hiện điều đó.
def cau_9():
    print("\n--- CÂU 9: MA TRẬN TƯƠNG QUAN ---")
    plt.figure(figsize=(15,7))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('mối tương quan giữa budget, revenue, runtime, và vote_count')
    plt.show()

# Câu 10 (CÂU CHỐT): Bạn hãy tìm ra "Thể loại chính" (main_genre) nào có 
# điểm đánh giá trung bình cao nhất?
def cau_10():
    print("\n--- CÂU 10: THỂ LOẠI ĐỈNH NHẤT ---")
    best_genre = df.groupby('main_genre')['vote_average'].sum().head(1)
    print('thể loại phim có lượt vote nhiều nhất là: \n', best_genre)

# --- THỰC THI ---
if __name__ == "__main__":
    cau_10()


    