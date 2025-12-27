#!/bin/python3

import math
import os
import random
import re
import sys

# --- Bước 1: Đọc N và M ---
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

# --- Bước 2: Đọc ma trận ---
# Chúng ta đọc từng dòng đầy đủ, không dùng .split()
# vì dấu cách ' ' cũng là một ký tự hợp lệ trong ma trận.
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# --- Bước 3: Giải mã ma trận (Duyệt theo cột) ---
# Ý tưởng của bạn đã đúng: duyệt cột trước, hàng sau.
# Vòng lặp ngoài là cột (từ 0 đến m-1)
# Vòng lặp trong là hàng (từ 0 đến n-1)

decoded_chars = []
for j in range(m):  # j là chỉ số cột
    for i in range(n):  # i là chỉ số hàng
        # Lấy ký tự tại [hàng][cột]
        decoded_chars.append(matrix[i][j])

# Nối tất cả ký tự lại để được chuỗi thô
# Ví dụ: "This$#is% Matrix# %!"
raw_script = "".join(decoded_chars)

# --- Bước 4: Dọn dẹp chuỗi bằng Regex (không dùng 'if') ---
# Đây là phần mấu chốt.
# Chúng ta muốn thay thế "một hoặc nhiều ký tự đặc biệt/dấu cách"
# NẰM GIỮA "hai ký tự chữ/số" bằng MỘT dấu cách.

# Phân tích Regex: r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])'
#
# (?<=[A-Za-z0-9]) : Positive Lookbehind (Khẳng định Phía sau)
#                   Đảm bảo rằng chuỗi ký tự đặc biệt phải được đứng SAU
#                   một ký tự chữ hoặc số (A-Z, a-z, 0-9).
#
# ([^A-Za-z0-9]+)   : Nhóm ký tự cần tìm (The Match)
#                   Tìm 1 hoặc nhiều ký tự (+) KHÔNG PHẢI (^) là
#                   chữ hoặc số. Đây chính là các ký hiệu và dấu cách.
#
# (?=[A-Za-z0-9])  : Positive Lookahead (Khẳng định Phía trước)
#                   Đảm bảo rằng chuỗi ký tự đặc biệt phải được đứng TRƯỚC
#                   một ký tự chữ hoặc số.
#
# re.sub(..., ' ', raw_script):
#                   Tìm tất cả các mẫu khớp với regex trên trong `raw_script`
#                   và thay thế chúng bằng một dấu cách duy nhất ' '.

final_script = re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])', ' ', raw_script)

print(final_script)