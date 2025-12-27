n1 = int(input())
student_number_1 = set(map(int,input().split()))
n2 = int(input())
student_number_2 = set(map(int,input().split()))

# toán tử & nghĩa là phần chung giữa 2 tập hợp
common_part = student_number_1 & student_number_2
print(len(common_part))

# hoặc có thể dùng  .intersection() để biểu diễn tương tự như toán tử &
common_part_2 = student_number_1.intersection(student_number_2)
print(common_part_2)