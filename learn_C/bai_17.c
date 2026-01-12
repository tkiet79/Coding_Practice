/*Bài 3: Duyệt mảng không dùng [i]

Viết hàm tính tổng các phần tử trong mảng.

Luật: Tuyệt đối không dùng arr[i]. Hãy dùng con trỏ ptr để duyệt từ đầu đến cuối mảng (ptr++).*/

#include<stdio.h>
long long Sum(long long *arr, int n);
int main() {
    long long n;
    printf("nhap kich thuoc mang: "); scanf("%lld",&n);
    long long arr[n];
    long long i;
    for (i=0; i<n; i++) {
        printf("\nnhap gia tri cac gia tri trong mang: "); scanf("%lld", &arr[i]);
    }
    long long total = Sum(arr,n);
    printf("tong cac gia tri trong mang la: %lld", total);
    return 0;
}

long long Sum(long long *arr, int n) {
    long long *ptr = arr;
    long long total = 0;
    long long *end = arr + n; 
    while (ptr < end) {
        total += *ptr;
        ptr++;

    }
    return total;
}
