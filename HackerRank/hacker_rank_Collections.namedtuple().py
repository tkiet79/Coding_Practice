from collections import namedtuple

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------CODE TINH GỌN-----------------------------------------#
N = int(input());student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)


#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------CODE ĐẦY ĐỦ-----------------------------------------#
# 1. Đọc số lượng sinh viên
N = int(input()) 

# 2. Đọc tên các cột và tạo "khuôn mẫu" (blueprint) cho sinh viên
#    Input ví dụ: "ID MARKS NAME CLASS"
column_names_line = input()
column_names_list = column_names_line.strip().split() 
# column_names_list bây giờ là ['ID', 'MARKS', 'NAME', 'CLASS']

# Tạo một "lớp" (khuôn mẫu) tên là 'student'
# với các thuộc tính (nhãn) là tên các cột
student = namedtuple('student', column_names_list)

# 3. Đọc N dòng thông tin sinh viên và lưu điểm
total_marks = 0
for i in range(N):
    # Đọc thông tin một sinh viên
    # Input ví dụ: "1 97 Ram_G Y"
    student_data_line = input()
    student_data_list = student_data_line.strip().split()
    # student_data_list bây giờ là ['1', '97', 'Ram_G', 'Y']
    
    # Dùng "khuôn mẫu" student để tạo một sinh viên cụ thể
    # Dấu * sẽ "giải nén" list:
    # student(*['1', '97', 'Ram_G', 'Y'])
    # ...tương đương với...
    # student('1', '97', 'Ram_G', 'Y')
    
    s = student(*student_data_list)
    
    # 4. Lấy điểm (MARKS) của sinh viên đó
    # Đây là điểm sướng nhất của namedtuple:
    # thay vì dùng s[1] (khó nhớ), ta dùng s.MARKS (rõ ràng)
    mark_string = s.MARKS 
    
    # Chuyển điểm từ chữ (string) sang số (float)
    mark_float = float(mark_string)
    
    # Cộng vào tổng điểm
    total_marks = total_marks + mark_float

# 5. Tính và in ra điểm trung bình
average = total_marks / N
print(average)