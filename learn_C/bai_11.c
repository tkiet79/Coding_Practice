/*Bài 1: "Cỗ máy tính toán" (Cơ bản)

Mục tiêu: Hiểu cách truyền tham chiếu vào hàm để lấy nhiều kết quả trả về.

Đề bài:
Viết một hàm tên là calculate nhận vào 2 số nguyên a, b và 2 con trỏ sum, diff.
Hàm này không trả về gì cả (void), nhưng sau khi chạy xong, biến sum phải chứa tổng, biến diff phải chứa hiệu của a và b.*/

#include<stdio.h>

void calculate(int a, int b, long long  *sum, long long  *diff);
int main (void) {
    printf("nhap 2 so nguyen bat ky: ");
    long long x,y;

    scanf("%d%d",&x,&y);

    long long int tong, hieu; 

    calculate(x,y,&tong,&hieu);

    printf("tong: %lld, hieu: %lld",tong, hieu);

    return 0;
}

void calculate(int a, int b, long long  *sum, long long  *diff) {
    *sum = a + b;
    *diff = a - b;
}
