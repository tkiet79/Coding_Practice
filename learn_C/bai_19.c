/*Bài 5: Kiểm tra Palindrome (Đối xứng)

Viết hàm kiểm tra một chuỗi có đối xứng không (ví dụ: "radar", "madam" là có; "hello" là không).

Gợi ý: Dùng kỹ thuật 2 con trỏ: Một con trỏ start ở đầu, một con trỏ end ở cuối, so sánh rồi di chuyển dần vào giữa.*/

int is_Palindrome(char *str, int n);
#include<stdio.h>
#include <string.h>
int main (void) 
{
    char str[100];
    printf("enter your string: ");
    fgets(str, 100, stdin);  
    int len = strlen(str);
    if (len > 0 && str[len - 1] == '\n') {
        str[len - 1] = '\0'; // Xóa nó đi (thay bằng kết thúc chuỗi)
        len--; // Giảm độ dài thật
    }     
    // str + len   -> Trỏ vào ký tự '\0' (cuối cùng của bộ nhớ)
    // str + len - 1 -> Trỏ vào chữ 'o' (ký tự cuối cùng của dữ liệu)
    int res = is_Palindrome( str, len);
    if (res == 1) 
    {
        printf("day la mot chuoi Palindrome");
    } 
    else 
    {
        printf("day khong phai la mot chuoi Palindrome");
    }
    return 0;
}

int is_Palindrome(char *str,int n)
{
    char *start = str;
    char *end = str + n - 1;
    while (start < end)
    {
        if (*start != *end)
        {
            return 0;
        }
        start++;
        end--;
    }
    return 1;
}
