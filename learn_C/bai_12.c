/*Bài 2: "Gọng kìm" (Con trỏ & Mảng)

Mục tiêu: Sử dụng kỹ thuật 2 con trỏ (Two Pointers) để duyệt mảng, thay vì dùng index i.

Đề bài:
Viết hàm reverseArray nhận vào một mảng và kích thước của nó. Hãy đảo ngược mảng đó ngay lập tức (in-place) dùng con trỏ.

Không được dùng mảng phụ.

Không được dùng cú pháp arr[i]. Hãy dùng *ptr.*/

#include<stdio.h>
void reverseArray(int arr[], int size);
int main(void) {
    int size;
    printf("nhap kich thuoc mang: "); scanf("%d", &size);
    int arr[size];
    int i;
    for (i=0;i<size;i++) {
        printf("nhap gia tri cua mang: ");
        scanf("%d",&arr[i]);
    }
    reverseArray(arr, size);
    int j;
    printf("mang sau khi dao nguoc la: ");
    for (j=0;j<size;j++) {
        printf("%d ", arr[j]);
    }
}
void reverseArray(int arr[], int size) {
    int *start = arr;
    int *end = (arr + size - 1);
    int temp;
    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start += 1;
        end -= 1;
    }
}