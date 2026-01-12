/*Bài 2: Con trỏ tìm Max

Viết hàm findMax nhận vào mảng arr và kích thước n.

Yêu cầu: Hàm không trả về giá trị lớn nhất (ví dụ số 99), mà trả về con trỏ trỏ tới số lớn nhất đó (địa chỉ của số 99).

Signature: int* findMax(int *arr, int n);

Test: Trong main, in ra giá trị tại địa chỉ mà hàm trả về.*/

#include<stdio.h>
int* findMax(int *arr, int n);
int main() {
    int n;
    printf("nhap kich thuoc mang: "); scanf("%d", &n);
    int i, arr[n];
    for (i=0;i<n;i++) {
        printf("\nnhap gia tri cua mang: ");
        scanf("%d", &arr[i]); 
    }
    int* res = findMax(arr,n);
    printf("dia chi cua gia tri lon nhat trong mang la: %p",(void*)res);
    return 0;
}

int* findMax(int *arr, int n) {
    if (n <= 0) return NULL;

    int *maxaddress = arr;
    int i;
    for (i=1; i<n; i++) {
        if (*(arr + i) > *maxaddress) {
            maxaddress = (arr + i);
        }
    }
}
