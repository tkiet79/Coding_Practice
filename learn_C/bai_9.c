/*Bài 9: Đảo ngược mảng 

Đề bài: Nhập mảng n phần tử. Đảo ngược thứ tự các phần tử trong mảng 
(ví dụ: [1, 2, 3] thành [3, 2, 1]) và in mảng sau khi đảo ngược ra màn hình.
Mục tiêu: Tư duy về chỉ số (index) đầu và cuối, hoán đổi vị trí. */
#include<stdio.h>
int main() {
    
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int res[n];
    int i;
    for (i=n-1;i>=0;i--) {
        printf("%d ", arr[i]);
    }
    return 0;
}