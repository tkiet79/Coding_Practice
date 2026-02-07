import pandas as pd
import numpy as np

data = {
    'EmpID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'FullName': ['Nguyen Van An', 'Le Thi Binh', 'Tran Hoang Chi', 'Nguyen Van An', 'Pham Minh Dong', 'Le Thi Binh', 'Hoang Quoc An', 'Vu Thi Chi', 'Pham Minh Dong', 'Doan Van Em'],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'Finance', 'HR', 'IT', 'Sales', 'Finance', 'IT'],
    'Salary': [1500, 1200, 1600, np.nan, 1800, 1250, 1550, 900, np.nan, 1400],
    'JoiningDate': ['2020-01-10', '2019-05-15', '2021-03-20', '2022-11-01', '2018-08-12', '2019-06-01', '2020-12-15', '2023-02-10', '2017-09-25', '2021-01-05'],
    'City': ['Hanoi', 'HCM', 'Hanoi', 'Danang', 'Hanoi', 'HCM', 'Danang', 'Hanoi', 'HCM', 'Hanoi'],
    'Remote': ['Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
# Bài 1: Tổng quan hệ thống
# Yêu cầu: Xem 5 dòng đầu và kiểm tra xem cột nào đang bị thiếu dữ liệu (isnull().sum()).
missing_value = df.head(5).isnull().sum()
# Bài 3: Xử lý dữ liệu thiếu (Data Cleaning)
# Yêu cầu: Những người có Salary bị trống (NaN), hãy điền cho họ giá trị bằng trung bình lương của cả công ty.
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# Bài 2: Tính thu nhập năm
# Yêu cầu: Tạo cột AnnualSalary bằng cách lấy Salary * 12. (Đừng lo về giá trị NaN lúc này).
df['AnnualSalary'] = df['Salary'] * 12
# Bài 4: Tách tên (String Manipulation)
# Yêu cầu: Tạo cột FirstName bằng cách lấy từ cuối cùng trong cột FullName.
df['Firstname'] = df['FullName'].str.split().str[-1].str.strip()
# Bài 5: Lọc nhân sự kỳ cựu
# Yêu cầu: Lọc ra những nhân viên vào làm trước năm 2020 (từ 31/12/2019 trở về trước).
df['IsSenior'] = df['JoiningDate'].dt.year < 2020
# Bài 6: Thống kê lương theo phòng ban
# Yêu cầu: Tính mức lương trung bình (Salary) của từng phòng ban (Department).
Revenue_per_Department = df.groupby('Department')['Salary'].mean()
# Câu 8: Thống kê xem có bao nhiêu nhân viên đang làm việc theo hình thức Remote ('Yes') 
# và bao nhiêu người làm tại văn phòng 
remote_employee_count = df['Remote'].value_counts()
# Câu 9: Tìm mức lương cao nhất đang được chi trả tại mỗi thành phố (City)
highest_salary = df.groupby('City')['Salary'].max()
# Câu 10: Tạo một bảng Pivot Table để đếm số lượng nhân viên của mỗi phòng ban tại mỗi thành phố khác nhau.
Summaries = pd.pivot_table(df, values='EmpID', index='Department', columns='City', aggfunc='count', fill_value=0)
print(df)
print(remote_employee_count)
print(highest_salary)
print(Summaries)


