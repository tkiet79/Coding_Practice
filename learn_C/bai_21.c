/*Bài 1: Mảng động co giãn (Dynamic Int Array) - Level 1.5

Mục tiêu: Hiểu malloc, realloc và quản lý mảng số nguyên.

Yêu cầu:
1. Viết chương trình nhập vào một số nguyên n.
2. Dùng malloc tạo một mảng chứa n số nguyên.
3. Nhập dữ liệu cho mảng này từ bàn phím.
Thao tác co giãn:
4. Tự động dùng realloc để tăng kích thước mảng lên gấp đôi (2*n).
5. Các phần tử mới (từ vị trí n đến 2n-1) gán giá trị bằng 0.
6. In ra toàn bộ mảng (kích thước 2n) và free bộ nhớ.*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(void) 
{
    // bước 1. nhập vào một số nguyên n.
    int n;
    printf("nhap kich thuoc mang: "); 
    if (scanf("%d", &n) != 1 || n <= 0) 
    {
        printf("Input khong hop le!\n");
        return 1;
    }

    // bước 2. Dùng malloc tạo một mảng chứa n số nguyên.
    int *arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL)
    {
        fprintf(stderr, "Khong du bo nho!\n");
        exit(1);
    }

    // bước 3. Nhập dữ liệu cho mảng này từ bàn phím.
    for (int i = 0; i < n ; i++)
    {
        printf("Nhap gia tri thu %d: ", i + 1);
        scanf("%d",&arr[i]);
    }

    // bước 4. Tự động dùng realloc để tăng kích thước mảng lên gấp đôi (2*n).
    int *temp = (int*)realloc(arr, (2*n) * sizeof(int));
    if (temp == NULL)
    {
        fprintf(stderr, "Khong the mo rong bo nho!\n");
    } 

    else 
    {
        arr = temp;
    }

    // bước 5. Các phần tử mới (từ vị trí n đến 2n-1) gán giá trị bằng 0.
    for (int i = n; i < 2 * n; i++) {
        arr[i] = 0;
    }

    //bước 6. In ra toàn bộ mảng (kích thước 2n) và free bộ nhớ.
    for (int i = 0; i < 2*n; i++)
    {
        printf("%d ",arr[i]);
    }
    free(arr);
    return 0;

}