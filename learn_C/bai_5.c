/*Bài 5: Tính tổng từ 1 đến N
Đề bài: Nhập số nguyên dương n. Tính tổng S = 1 + 2 + ... + n. */

#include<stdio.h>
int Sum(int);

int main(void) {
    int n;
    printf("enter your number: ");
    scanf("%d", &n);
    int res = Sum(n);
    printf("answer is %d", res);
    return 0;
}

int Sum(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return Sum(n-1) + n;
    }
}