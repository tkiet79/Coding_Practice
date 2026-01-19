/*
 * ALL-IN-ONE FILE MANAGER (READ - WRITE - CLEAR)
 * Author: Sếp
 * * Bài học QUAN TRỌNG: 
 * 1. Logic "Wipe" (Xóa sạch): fclose -> fopen("w") -> fclose -> fopen("a+").
 * 2. Phân biệt lệnh điều khiển ("exit", "clear") và dữ liệu thông thường.
 * 3. Kiểm soát con trỏ file chặt chẽ.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hàm tiện ích để mở lại file mode a+ (đỡ phải viết lại nhiều lần)
FILE* open_file_append() {
    FILE *f = fopen("test.txt", "a+");
    if (f == NULL) {
        perror("Loi nghiem trong: Khong the mo file!");
        exit(1);
    }
    return f;
}

int main() {
    FILE *fptr;
    char buffer[100]; 

    printf("--- CHUONG TRINH QUAN LY FILE TOAN DIEN ---\n");
    printf("Cac lenh dac biet:\n");
    printf("  - 'exit' : Luu va thoat chuong trinh.\n");
    printf("  - 'clear': XOA SACH du lieu trong file hien tai.\n");
    printf("  - Con lai: Noi dung se duoc ghi vao file.\n");
    printf("--------------------------------------------------\n");

    // Mở file lần đầu
    fptr = open_file_append();

    // Hiện lịch sử cũ (nếu có)
    printf("\n[LICH SU] Noi dung hien tai:\n");
    rewind(fptr); 
    int hasData = 0;
    while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
        printf("  > %s", buffer);
        hasData = 1;
    }
    if (!hasData) printf("  (File dang trong)\n");
    printf("----------------------------------\n");

    // Đưa con trỏ về cuối để sẵn sàng ghi
    fseek(fptr, 0, SEEK_END);
    
    while (1) {
        printf("Nhap lenh/noi dung: ");
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) break;

        // Xử lý xóa dấu xuống dòng
        buffer[strcspn(buffer, "\n")] = 0;

        // --- XỬ LÝ LỆNH ---

        // 1. Lệnh EXIT
        if (strcmp(buffer, "exit") == 0) {
            printf("[INFO] Dang luu va thoat...\n");
            break;
        }

        // 2. Lệnh CLEAR (Xóa sạch file)
        if (strcmp(buffer, "clear") == 0) {
            printf("[ACTION] Dang xoa sach du lieu trong file...\n");
            
            // Bước 1: Đóng kết nối hiện tại
            fclose(fptr);

            // Bước 2: Mở lại mode "w" (Write) -> Hành động này sẽ TRUNCATE (xóa trắng) file
            fptr = fopen("test.txt", "w"); 
            if (fptr == NULL) { perror("Loi khi xoa file"); return 1; }
            
            // Bước 3: Đóng lại ngay (vì ta chỉ cần nó xóa thôi)
            fclose(fptr);

            // Bước 4: Mở lại mode "a+" để tiếp tục nhập liệu
            fptr = open_file_append();

            printf("[OK] File da duoc xoa trang. Tiep tuc nhap lieu moi:\n");
            continue; // Bỏ qua phần ghi bên dưới, quay lại đầu vòng lặp
        }

        // --- XỬ LÝ GHI DỮ LIỆU ---
        
        // Nếu không phải lệnh đặc biệt, ghi vào file
        fprintf(fptr, "%s\n", buffer);
        fflush(fptr); // Lưu ngay lập tức
        printf("   -> Da ghi.\n");
    }

    // Đóng file lần cuối
    if (fptr) fclose(fptr);
    
    printf("\n[XONG] Chuong trinh ket thuc.\n");
    
    printf("Nhan Enter de thoat...");
    getchar();
    return 0;
}