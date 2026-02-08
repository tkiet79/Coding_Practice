import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột, không bị dấu ...
pd.set_option('display.width', 150)         # Ép độ rộng hiển thị ra 1000 ký tự để không bị xuống dòng
pd.set_option('display.colheader_justify', 'center') # Căn giữa tiêu đề cho đẹp
pd.set_option('display.expand_frame_repr', False)
data = {
    'Movie_ID': range(1, 11),
    'Title': [' the dark knight ', 'Inception', 'interstellar', 'Parasite', 'The Avengers', ' inception', 'Joker', 'Avengers: Endgame', 'Parasite', 'The Lion King'],
    'Genre': ['Action|Drama', 'Sci-Fi|Action', 'Sci-Fi|Drama', 'Thriller|Drama', 'Action', 'Sci-Fi|Action', 'Crime|Drama', 'Action|Sci-Fi', 'Thriller|Drama', 'Animation|Adventure'],
    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Bong Joon-ho', 'Joss Whedon', 'Christopher Nolan', 'Todd Phillips', 'Anthony Russo', 'Bong Joon-ho', 'Jon Favreau'],
    'Release_Year': [2008, 2010, 2014, 2019, 2012, 2010, 2019, 2019, 2019, 2019],
    'Runtime_Min': [152, 148, 169, 132, 143, 148, 122, 181, 132, 118],
    'Rating': [9.0, 8.8, 8.6, 8.6, 8.0, 8.8, 8.4, 8.4, np.nan, 6.9],
    'Revenue_Millions': [534.8, 292.5, 188.0, 53.3, 623.3, 292.5, 335.4, 858.3, 53.3, 543.6],
    'Votes': [2300000, 2000000, 1500000, 550000, 1200000, 2000000, 950000, 850000, 550000, 210000]
}
df = pd.DataFrame(data)

# Câu 1 (Dọn dẹp tiêu đề): Cột Title đang bị dính khoảng trắng ở đầu/cuối và viết hoa lộn xộn. 
# Hãy dùng .str.strip() và .str.title() để chuẩn hóa lại tên phim.
df['Title'] = df['Title'].str.strip().str.title()

#Câu 2 (Xử lý trùng lặp): Trong dữ liệu có những bộ phim bị lặp lại hoàn toàn (do lỗi nhập liệu). 
# Hãy loại bỏ các dòng trùng lặp (drop_duplicates) và chỉ giữ lại một dòng duy nhất cho mỗi phim.
df.drop_duplicates(subset=['Title'])

# Câu 3 (Xử lý dữ liệu thiếu): Kiểm tra cột Rating. 
# Nếu có giá trị thiếu, hãy điền bằng giá trị trung bình (mean) của các phim cùng Director đó.
df['Rating'] = df['Rating'].fillna(df.groupby('Director')['Rating'].transform('mean'))

# Câu 4 (Tách chuỗi phức tạp): Cột Genre chứa nhiều thể loại cách nhau bởi dấu gạch đứng |. 
# Hãy tạo một cột mới Main_Genre chỉ lấy thể loại đầu tiên của mỗi phim.
df['Main_Genre'] = df['Genre'].str.split('|').str[0]

# Câu 5 (Tư duy Vectorized): Tạo cột Score_Per_Minute bằng cách lấy Rating chia cho Runtime_Min.
# Phim nào có "mật độ chất lượng" cao nhất?
df['Score_Per_Minute'] = df['Rating'] / df['Runtime_Min']
highest_density = df['Score_Per_Minute'].sort_values(ascending=False).head(1)

# Câu 6 (Phân loại phim): Tạo cột Movie_Type. Nếu Runtime_Min < 120 thì là 'Short', 
# từ 120 - 150 là 'Medium', trên 150 là 'Epic'.
df['Movie_Type'] = df['Runtime_Min'].apply(lambda x: "Epic" if x > 150 else "Short" if x < 120 else "Medium")

# Câu 7 (Lọc dữ liệu): Lấy ra danh sách các phim của đạo diễn 'Christopher Nolan' có Rating > 8.5
high_rating_of_Christopher_Nolan = df[(df['Director'] == 'Christopher Nolan') & (df['Rating'] > 8.5)] 

# Câu 8 (Thống kê theo năm): Tính tổng doanh thu (Revenue_Millions) 
# và điểm đánh giá trung bình theo từng năm phát hành.
yearly_summary = df.groupby('Release_Year').agg({
    'Revenue_Millions': 'sum',
    'Rating': 'mean' # Dùng mean cho đúng nghĩa "trung bình"
}).rename(columns={'Revenue_Millions': 'Total_Revenue', 'Rating': 'Average_Rating'})

# Câu 9 (Hàm Lambda nâng cao): Tạo cột Is_Blockbuster. 
# Một bộ phim được coi là Blockbuster (True) nếu nó có Revenue_Millions > 300 VÀ Votes > 1,000,000
df['Is_Blockbuster'] = df.apply(lambda row: row['Revenue_Millions'] > 300 and row['Votes'] > 1000000, axis=1)

# Câu 10 (Pivot Table): Tạo bảng Pivot Table hiển thị tổng doanh thu của mỗi đạo diễn (Director) theo từng năm (Release_Year). 
# Những ô không có dữ liệu hãy điền là 0.
Summary = pd.pivot_table(df, 
                         values='Revenue_Millions', 
                         index='Director', 
                         columns='Release_Year', 
                         aggfunc='sum', 
                         fill_value=0)

print(df)
print(Summary)
