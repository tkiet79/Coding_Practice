/*Bài 7: Tìm số lớn nhất trong mảng

Đề bài: 
1. Nhập số nguyên n (số lượng phần tử của mảng).
2. Nhập n số nguyên vào mảng.
3. Tìm và in ra giá trị lớn nhất trong mảng đó.

Mục tiêu: Làm quen với cách khai báo mảng, duyệt mảng bằng vòng lặp và thuật toán tìm kiếm cơ bản. */

#include<stdio.h>

int main(void) {
    int n;
    int arr[n];
    int i;
    int value;
    int max_value = 0;
    printf("enter your size of arr: ");
    scanf("%d", &n);
    
    for (i=0;i<n;i++) {
        printf("enter your value: ");
        scanf("%d", &value);
        arr[i] = value;
        if (value > max_value) {
            max_value = value;
        }
    }
    printf("max value in arr is:  %d", max_value);
    return 0;
}