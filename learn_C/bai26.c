#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// BÀI 1: my_atoi (String to Integer)
// ==========================================
// Giống hàm int() của Python hoặc atoi() của C.
// Yêu cầu:
// 1. Bỏ qua khoảng trắng ở đầu.
// 2. Xử lý dấu (+ hoặc -).
// 3. Chuyển đổi các ký tự số thành số nguyên.
// 4. Dừng khi gặp ký tự không phải số.
// VD: "   -1234abc" -> -1234
int my_atoi(const char *str) {
    if (str == NULL) return 0;
    
    int result = 0;
    int sign = 1;
    int i = 0;

    // 1. Bỏ qua khoảng trắng
    while (isspace(str[i])) {
        i++;
    }
    
    // 2. Check dấu
    if (str[i] == '-' || str[i] == '+') {
        if (str[i] == '-') {
            sign = -1;
        }
        i++; 
    }
    
    // 3. Duyệt qua từng số
    while (isdigit(str[i])) {
        // [FIXED] Lỗi sai của mày nằm ở đây.
        // Mày phải trừ đi '0' (ASCII 48) để ra giá trị số thực.
        // VD: '5' (53) - '0' (48) = 5.
        // Công thức chuẩn: result = result * 10 + (digit_value)
        result = result * 10 + (str[i] - '0');
        i++;
    }
    
    return result * sign;
}