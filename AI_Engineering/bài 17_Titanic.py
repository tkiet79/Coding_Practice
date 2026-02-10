import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. TRIỆU HỒI DỮ LIỆU ---
# Tao dùng dữ liệu trực tiếp từ thư viện Seaborn cho nhanh
try:
    df = sns.load_dataset('titanic')
    print("--- ĐÃ TẢI DỮ LIỆU TITANIC THÀNH CÔNG ---")
except:
    # Backup link nếu máy mày không có seaborn
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print("--- ĐÃ TẢI DỮ LIỆU TỪ LINK BACKUP ---")

# survived:    Sống sót (0 = Chết, 1 = Sống)
# pclass:      Hạng vé (1 = Hạng nhất, 2 = Hạng hai, 3 = Hạng ba)
# sex:         Giới tính (male = nam, female = nữ)
# age:         Tuổi
# sibsp:       Số lượng anh chị em hoặc vợ/chồng đi cùng trên tàu
# parch:       Số lượng cha mẹ hoặc con cái đi cùng trên tàu
# fare:        Giá vé (Số tiền hành khách đã trả)
# embarked:    Cổng lên tàu (C = Cherbourg, Q = Queenstown, S = Southampton)
# class:       Hạng vé (Tương tự pclass nhưng ở dạng chữ: First, Second, Third)
# who:         Phân loại (man = đàn ông, woman = phụ nữ, child = trẻ em)
# adult_male:  Có phải đàn ông trưởng thành hay không (True/False)
# deck:        Boong tàu (Vị trí phòng ở trên các tầng của tàu)
# embark_town: Tên thành phố nơi hành khách lên tàu
# alive:       Còn sống hay không (yes/no - tương ứng với survived)
# alone:       Đi một mình hay không (True = đi một mình, False = đi cùng gia đình)
print("-" * 100)

# =========================================================================
# CHẶNG 1: SINH TỒN TRONG "RÁC" (DATA CLEANING)
# =========================================================================

# Câu 1: Kiểm tra xem có bao nhiêu "linh hồn" bị mất tích (NaN) ở mỗi cột.
# Cột nào có tỷ lệ mất tích trên 70% thì hãy mạnh tay XÓA bỏ cột đó luôn.
missing_counts = df.isnull().sum()
threshold = 0.7 * len(df)
cols_to_drop = missing_counts[missing_counts > threshold].index.tolist()
df = df.drop(columns=cols_to_drop)

# Câu 2: Cột 'age' (tuổi) rất quan trọng. Hãy điền các giá trị thiếu bằng:
# Trung vị (median) của tuổi THEO TỪNG NHÓM (Giới tính & Hạng vé - Pclass).
df['age'] = df['age'].fillna(df.groupby(['sex', 'pclass'])['age'].transform('median'))

# =========================================================================
# CHẶNG 2: GIẢI MÃ GEN (FEATURE ENGINEERING)
# =========================================================================

# Câu 3: Tạo cột 'Family_Size' = số lượng người thân đi cùng (sibsp + parch + 1).
# Sau đó tạo tiếp cột 'Is_Alone': 1 nếu đi một mình, 0 nếu đi với gia đình.
df['Family_Size'] = df['sibsp'] + df['parch'] + 1
df['Is_Alone'] = df['alone'].apply(lambda x: 1 if x == True else 0)

# Câu 4: Phân loại giá vé (Fare). Tạo cột 'Fare_Category' với 4 mức: 
# 'Cheap', 'Standard', 'Expensive', 'Luxury' dựa trên các khoảng tứ phân vị (Quartiles).
# Gợi ý: Dùng pd.qcut()
df['Fare_Category'] = pd.qcut(df['fare'], q=4, labels=['Cheap', 'Standard', 'Expensive', 'Luxury'])

# =========================================================================
# CHẶNG 3: TRUY TÌM SỰ THẬT (DEEP ANALYSIS)
# =========================================================================

# Câu 5: Tính tỷ lệ sống sót (Survival Rate) theo Giới tính (Sex). 
# Ai là người có cơ hội sống sót cao hơn?
survival_by_sex = df.groupby('sex')['survived'].mean()
print(survival_by_sex)
print(f"Nhận xét: Phụ nữ có tỷ lệ sống sót cao gấp khoảng {survival_by_sex['female']/survival_by_sex['male']:.1f} lần nam giới!")

# Câu 6: Dùng Pivot Table để xem tỷ lệ sống sót kết hợp giữa: 
# Hạng vé (class) và Nơi khởi hành (embark_town).
print()
print("tỉ lệ sống sót giữa các hạng vé và nơi khởi hành: ")
summary = df.pivot_table(values = 'survived', index = 'pclass', columns = 'embarked', aggfunc = 'mean', fill_value=0)
#print(summary)

# Câu 7: Tìm 5 hành khách có "mệnh lớn" nhất (Giá vé rẻ nhất nhưng vẫn sống sót).
lucky_pas = df[df['survived'] == 1].sort_values('fare', ascending=True).head(5)
print(lucky_pas)

# =========================================================================
# CHẶNG 4: THỊ GIÁC HÓA (VISUALIZATION - LEVEL BOSS)
# =========================================================================

# Câu 8: Vẽ biểu đồ cột (Bar plot) so sánh số lượng người sống/chết theo từng Hạng vé (class).
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='class', hue='survived', palette='viridis')
plt.title('Số lượng người Sống (1) vs Chết (0) theo Hạng vé')
plt.xlabel('Hạng vé (Passenger Class)')
plt.ylabel('Số lượng hành khách')
plt.legend(title='Sống sót', labels=['Chết', 'Sống'])
plt.show()
# Câu 9: Vẽ biểu đồ phân phối tuổi (Histogram) của những người sống sót vs người chết.
# Xem thử có phải "Trẻ em luôn được ưu tiên" không?
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', hue='survived', kde=True, element="step", palette='magma')
plt.title('Phân phối độ tuổi theo trạng thái sống sót')
plt.xlabel('Tuổi (Age)')
plt.ylabel('Mật độ / Số lượng')
plt.legend(title='Sống sót', labels=['Sống', 'Chết']) # Đảo lại label cho khớp màu palette
plt.show()

# Câu 10 (CÂU CHỐT): Tính ma trận tương quan (Correlation Matrix) giữa các cột số.
# Cột nào có ảnh hưởng mạnh nhất đến việc 'survived' (sống sót)?
plt.figure(figsize=(12, 8))
# Lưu ý: Chỉ tính tương quan trên các cột có kiểu dữ liệu số
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Ma trận tương quan giữa các đặc trưng số')
plt.show()

print(df)
print("\n--- KẾT THÚC ĐẤU TRƯỜNG ---")