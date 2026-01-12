#include <stdio.h>
#include <stdlib.h> // THƯ VIỆN BẮT BUỘC để dùng malloc và free

int main() {
    int n;
    int *arr; // Con trỏ để quản lý vùng nhớ sắp xin
    // 1. Hỏi người dùng số lượng phần tử cần dùng
    printf("Ban muon nhap bao nhieu so? ");
    scanf("%d", &n);
    // 2. Cấp phát động (Xin đất từ bộ nhớ Heap)
    // Cú pháp: (kiểu dữ liệu*) malloc(số lượng * kích thước 1 phần tử)
    // Ví dụ: n = 5, int = 4 bytes => xin 20 bytes
    arr = (int*)malloc(n * sizeof(int));
    // KIỂM TRA QUAN TRỌNG:
    // Nếu hết RAM, malloc sẽ trả về NULL. Phải kiểm tra để tránh lỗi chương trình.
    if (arr == NULL) {
        printf("Loi: Khong du bo nho RAM de cap phat!\n");
        return 1; // Thoát chương trình báo lỗi
    }
    // 3. Nhập dữ liệu
    // Sau khi malloc, 'arr' dùng y hệt như mảng bình thường arr[i]
    for (int i = 0; i < n; i++) {
        printf("Nhap so thu %d: ", i + 1);
        scanf("%d", &arr[i]); 
    }
    // 4. Tìm số lớn nhất (Max)
    // Giả sử phần tử đầu tiên là max
    int max = arr[0]; 
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("\n--> So lon nhat trong mang la: %d\n", max);

    // 5. QUAN TRỌNG NHẤT: Giải phóng bộ nhớ (Trả đất)
    // Nếu không free, vùng nhớ này bị chiếm dụng mãi cho đến khi tắt chương trình (Memory Leak)
    free(arr);
    printf("Da giai phong bo nho thanh cong!\n");

    return 0;
}