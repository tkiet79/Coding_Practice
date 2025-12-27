n1 = int(input())
student_number_1 = set(map(int,input().split()))
n2 = int(input())
student_number_2 = set(map(int,input().split()))

# toán tử - nghĩa là phần chỉ riêng trong 1 tập hợp mà các tập hợp khác không có
common_part = student_number_1 - student_number_2
print(len(common_part))

# hoặc có thể sử dụng .difference() để biểu diễn y hệt như toán tử -
common_part_2 = student_number_1.difference(student_number_2)
print(len(common_part_2))