/* Bài 9: Tìm kiếm giá trị (Linear Search) 

Đề bài:
1. Nhập mảng n phần tử.
2. Nhập một số x cần tìm.
3.Kiểm tra x có xuất hiện trong mảng không? Nếu có, in ra vị trí (index) đầu tiên tìm thấy. Nếu không, thông báo "Khong tim thay". 
Mục tiêu: Thuật toán tìm kiếm tuyến tính cơ bản */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void) {
    srand(time(NULL));
    long n, x;
    printf("nhap so luong phan tu: ");
    scanf("%d", &n);
    printf("nhap so can tim: ");
    scanf("%d", &x);
    long arr[n];
    long i;
    int res = 0;
    for(i=0 ; i < n;i++) {
        arr[i] = rand() % (100 - 1 + 1) + 1;
        if (arr[i] == x) {
            res = i;
            printf("gia tri can tim o vi tri: %d", res);  
            break;
        } 
    }
    if (res ==0) {
        printf("khong tim thay!!");
    }
    
    return 0;
}