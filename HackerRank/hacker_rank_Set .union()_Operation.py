
n1 = int(input())
student_number_1 = set(map(int,input().split()))
n2 = int(input())
student_number_2 = set(map(int,input().split()))

# cách 1: dùng toán tử & nghĩa là phần chung của 2 tập hợp
common_part = student_number_1 & student_number_2
total = len(student_number_1) + len(student_number_2) - len(common_part)
print(total)

# cách 2: dùng union() nghĩa là tất cả phần tử không giao nhau của 2 tập hợp
total_subscribers = student_number_1.union(student_number_2)
print(len(total_subscribers))