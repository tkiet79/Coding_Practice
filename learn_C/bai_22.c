/*Bài 2: Tự chế hàm strdup (String Duplication) - Level 2.0

Mục tiêu: Hiểu bản chất chuỗi trong C và cấp phát động cho chuỗi.

Bối cảnh:
Trong thư viện <string.h> có hàm strdup (không chuẩn ANSI C nhưng phổ biến). Tao muốn mày tự viết lại nó.

Yêu cầu:
    Viết hàm char *my_strdup(const char *src).
    Nhận vào một chuỗi src.
    Bên trong hàm: malloc một vùng nhớ mới có kích thước vừa đủ để chứa src (đừng quên +1 cho ký tự \0).
    Copy dữ liệu từ src sang vùng nhớ mới.
    Trả về con trỏ tới vùng nhớ mới.

Trong main:
    Khai báo chuỗi tĩnh: char original[] = "Code nhu mot Senior";
    Gọi char *copy = my_strdup(original);
    In copy ra màn hình.
    Thử sửa ký tự đầu tiên của copy thành 'M' (để chứng minh nó là bản sao độc lập).
    In lại cả original và copy.
    free(copy).*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *my_strdup(const char *src);

int main(void) 
{
    char original[] = "Code nhu mot Senior";
    printf("1. Chuoi ban dau (Original): %s\n", original);
    char *copy = my_strdup(original);
    if (copy == NULL) 
    {
        fprintf(stderr, "Loi: Khong du bo nho de copy!\n");
        return 1;
    }
    copy[0] = 'M';
    printf("\n--- Sau khi sua 'C' thanh 'M' o ban sao ---\n");
    
    printf("Original (van y nguyen):     %s\n", original);
    printf("Copy (da thay doi):          %s\n", copy);

    // 4. Dọn dẹp
    free(copy);
    
    return 0;
}

char *my_strdup(const char *src)
{
    if (src == NULL)
    {
        return NULL;
    }
    char *new_str = (char*)malloc(strlen(src) + 1);
    if (new_str == NULL)
    {
        return NULL;
    }
    strcpy(new_str, src);
    return new_str;
}