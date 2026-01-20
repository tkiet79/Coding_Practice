/*
 * BỘ ĐỀ LUYỆN TẬP CON TRỎ (LEVEL 2 -> 3)
 * Author: Sếp
 * * LUẬT CHƠI:
 * 1. Chỉ được viết code vào trong các hàm (chỗ có comment TODO).
 * 2. KHÔNG dùng các hàm có sẵn như memcpy, memmove (đối với bài 2).
 * 3. Quản lý bộ nhớ cho chặt, malloc phải có free (ở main tao đã free hộ, nhưng trong hàm mày phải malloc đúng).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ==========================================
// BÀI 1: In-place String Trim (Level 2)
// ==========================================
// Yêu cầu: 
// 1. Xóa khoảng trắng thừa ở ĐẦU chuỗi.
// 2. Xóa khoảng trắng thừa ở CUỐI chuỗi.
// 3. Ở GIỮA các từ chỉ giữ lại đúng 1 khoảng trắng.
// VD: "   Hello    World   " -> "Hello World"
//
// ĐIỀU KIỆN TỬ THẦN: 
// - KHÔNG được malloc mảng mới. 
// - Phải thao tác trực tiếp trên chuỗi `str` đưa vào (In-place).
// - Độ phức tạp thời gian O(N), không gian O(1).
void trim(char *str) 
{
    if (str == NULL) return;
    
    int reader = 0;
    int writer = 0;

    // BƯỚC 1: Bỏ qua toàn bộ khoảng trắng ở ĐẦU (Leading spaces)
    // "   Code..." -> reader nhảy đến chữ 'C'
    while (str[reader] == ' ') 
    {
        reader++;
    }

    while (str[reader] != '\0') {
        if (str[reader] != ' ') {
            // Nếu không phải khoảng trắng, cứ ghi vào
            str[writer++] = str[reader];
        } else {
            if (writer > 0 && str[writer - 1] != ' ') {
                str[writer++] = ' ';
            }
        }
        reader++;
    }

    if (writer > 0 && str[writer - 1] == ' ') {
        writer--;
    }

    // BƯỚC 4: Kết thúc chuỗi (QUAN TRỌNG NHẤT)
    str[writer] = '\0';
}

int main() 
{
    printf("=== TEST BAI 1: TRIM ===\n");
    char s1[] = "   Code    C   kho  qua   ";
    printf("Truoc: '[%s]'\n", s1);
    trim(s1);
    printf("Sau  : '[%s]'\n", s1); 
    // Kỳ vọng: "Code C kho qua"
}