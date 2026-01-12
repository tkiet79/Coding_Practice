/*Bài 3: "Thước đo thủ công" (Con trỏ & Chuỗi)

Mục tiêu: Hiểu bản chất chuỗi ký tự trong C kết thúc bằng \0 (NULL character).

Đề bài:
Trong C, chuỗi chỉ là mảng các ký tự (char). Hãy viết hàm myStrLen nhận vào một chuỗi char *s và trả về độ dài của chuỗi đó.

Cấm dùng hàm có sẵn strlen() trong thư viện <string.h>.

Hãy dùng con trỏ để duyệt.*/

#include<stdio.h>
int myStrLen(char str[]);
int main() {
    char str[] = "toi ten la tieu minh kiet";
    int res = myStrLen(str);
    printf("do dai cua mang la: %d", res);
    return 0;
}

int myStrLen(char str[]) {
    char *p = str;
    while (*p != '\0') {
        p++;
    }
    return p - str;
}