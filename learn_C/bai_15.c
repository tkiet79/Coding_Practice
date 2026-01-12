/*Bài 1: Hoán đổi thần thánh (Swap)

Viết hàm swap nhận vào 2 con trỏ số nguyên. Hàm thực hiện hoán đổi giá trị của 2 số đó.

Input: a = 5, b = 10

Output: a = 10, b = 5

Gợi ý: Dùng biến tạm temp. Chú ý tham số là int *a, int *b.*/

#include<stdio.h>
void swap(int *a, int *b);
int main() {
    int a = 5;
    int b = 10;
    printf("truoc khi swap thi a: %d, b: %d", a, b);
    swap(&a, &b);
    printf("\nsau khi swap thi a: %d, b: %d", a, b);
    return 0;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}