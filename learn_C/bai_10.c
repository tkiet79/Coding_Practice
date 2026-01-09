/*Bài 11: Sắp xếp mảng

Đề bài: Sắp xếp mảng theo thứ tự tăng dần.
Mục tiêu: Thuật toán hoán đổi (Interchange Sort hoặc Bubble Sort).*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// BUBBLE_SORT
long main() {
    srand(time(NULL));
    long  n;
    printf("enter size of arr: ");
    scanf("%d", &n);
    long  arr[n];
    long  i;
    long  j;
    long  temp;
    for (i=0;i<n;i++) {
        arr[i] = rand() % 100;
    }
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    for (i=0;i<n;i++) {
        printf("%d ", arr[i]);
    }
    return 0;
    
}

