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
// BÀI 24: In-place String Trim (Level 2)
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

int main() {
    printf("=== TEST BAI 1: TRIM ===\n");
    // Test case phức tạp hơn:
    // 1. Khoảng trắng đầu
    // 2. Nhiều khoảng trắng giữa
    // 3. Khoảng trắng cuối
    // 4. Chuỗi rỗng hoặc chỉ có dấu cách (để test vụ crash)
    char s1[] = "   Code    C   kho  qua   "; 
    char s2[] = "     "; // Test case tử thần của mày
    char s3[] = "";      // Test case rỗng

    printf("Test 1 Truoc: '[%s]'\n", s1);
    trim(s1);
    printf("Test 1 Sau  : '[%s]'\n", s1); 

    printf("Test 2 (Spaces) Truoc: '[%s]'\n", s2);
    trim(s2);
    printf("Test 2 (Spaces) Sau  : '[%s]'\n", s2);

    printf("Test 3 (Empty) Truoc: '[%s]'\n", s3);
    trim(s3);
    printf("Test 3 (Empty) Sau  : '[%s]'\n", s3);
    return 0;
}