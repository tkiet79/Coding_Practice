n1 = int(input())
student_number_1 = set(map(int,input().split()))
n2 = int(input())
student_number_2 = set(map(int,input().split()))

#toán tử ^ cho phép chúng ta lấy phần riêng của 2 tập hợp rồi hợp lại thành 1
symmetric_difference = student_number_1 ^ student_number_2
print(len(symmetric_difference))

#hoặc có thể dùng .symmetric_difference() cũng có thể được biểu diễn y chang như toán tử ^
symmetric_difference_2 = student_number_1.symmetric_difference(student_number_2)
print(len(symmetric_difference_2))