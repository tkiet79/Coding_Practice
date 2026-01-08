/* Bài 7: Thống kê mảng
Đề bài: Nhập mảng n phần tử.
1. Tính tổng các phần tử.
2. Tính trung bình cộng.
3. Đếm số lượng số chẵn và số lẻ.
Mục tiêu: Xử lý nhiều tác vụ trong một lần duyệt hoặc nhiều lần duyệt. */

#include <stdio.h>
#include <stdlib.h> // Thư viện chứa rand() và srand()
#include <time.h>   // Thư viện chứa time()

int main() {
    int n;
    printf("Nhap so luong phan tu: ");
    scanf("%d", &n);
    int arr[n];
    int total = 0;
    int even = 0, odd = 0;
    // 1. Khởi tạo seed (hạt giống) dựa trên thời gian hiện tại
    // Nếu thiếu dòng này, các số ngẫu nhiên sẽ GIỐNG HỆT nhau mỗi lần chạy
    srand(time(NULL));
    // 2. Tạo mảng random

    for (int i = 0; i < n; i++) {
        // Công thức random trong khoảng [min, max]: 
        // rand() % (max - min + 1) + min
        arr[i] = rand() % 100; 
        total += arr[i];
        if (arr[i] % 2 ==0) {
            even += 1;
        } else {
            odd += 1;
        }
    }
    float revenge = total / n;
    printf("tong cac gia tri la: %d", total);
    printf("\ntrung binh cong cua mang la: %.2f", revenge);
    printf("\nso luong gia tri chan la: %d", even);
    printf("\nso luong gia tri le la: %d", odd);
    return 0;
}
