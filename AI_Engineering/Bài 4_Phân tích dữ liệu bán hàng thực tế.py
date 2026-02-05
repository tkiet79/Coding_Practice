import pandas as pd
import numpy as np
# 1. Khởi tạo dữ liệu (Tao làm mẫu cho cái khung, tự điền data vào)
data = {
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product': ['iPhone', 'S23', 'Laptop', 'iPhone', 'Tablet', 'S23', 'Laptop', 'Mouse', 'Keyboard', 'iPhone'],
    'Quantity': [1, 2, 1, np.nan, 2, 1, 1, 5, 2, 1],
    'Price': [1000, 900, 1500, 1000, 300, 900, 1500, 20, 50, 1000],
    'OrderDate': ['2023-12-01', '2023/12/05', '12-10-2023', '2023-12-15', '2023-11-20', None, '2023-12-20', '2023-12-22', '2023-12-25', '2023-12-30'],
    'CustomerAddress': ['Số 1, Lê Lợi, TP.HCM', 'Số 5, Nguyễn Huệ, Hà Nội', 'Đường 10, Đà Nẵng', 'Số 2, CMT8, TP.HCM', 'Số 9, Hải Phòng', 'Số 3, TP.HCM', 'Số 4, Hà Nội', 'Số 7, Cần Thơ', 'Số 8, Đà Nẵng', 'Số 10, TP.HCM']
}
df = pd.DataFrame(data)
print(df)
print("-"*100)
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median()) # lấy trung vị của cột Quantity để làm giá trị thay thế cho nan
df = df.dropna(subset=['OrderDate']) # Dùng subset để chỉ xóa những hàng bị thiếu Ngày tháng.
df['OrderDate'] = pd.to_datetime(df['OrderDate'],errors='coerce')
df = df.dropna(subset=['OrderDate'])
df['TotalRevenue'] = df['Quantity'] * df['Price']
df['City'] = df['CustomerAddress'].str.split(',').str[-1].str.strip()
top_3 = df.groupby('Product')['TotalRevenue'].sum().sort_values(ascending=False).head(3) # sort hàm theo thứ tự giảm dần sau đó lấy 3 giá trị đầu tiên
hcm_dec = df[(df['City'] == 'TP.HCM') & (df['OrderDate'].dt.month == 12)]
print(df)
print(top_3)
print(hcm_dec)
