/*Bài 4: Đếm nguyên âm

Viết hàm nhận vào một chuỗi char *str. Đếm xem có bao nhiêu nguyên âm (u, e, o, a, i) trong đó. Dùng con trỏ để duyệt.*/

#include<stdio.h>

int count(char *str);
int main() 
{
    char str[100];
    printf("enter your string: ");

    // fgets(biến_chuỗi, số_lượng_tối_đa, luồng_nhập_từ_bàn_phím)
    fgets(str, 100, stdin);  
    int res = count(str);

    printf("so luong chu cai nguyen am la: %d", res);
    return 0;
    
}

int count(char *str)
{
    int quantity = 0;
    while (*str != '\0') {
        if (*str == 'u' || *str == 'e' || *str == 'o' || *str == 'a' || *str == 'i') {
            quantity += 1;
        }
        str ++;
    }
    return quantity;
}