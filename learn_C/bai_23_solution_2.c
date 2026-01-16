/**
 * SENIOR SOLUTION: DYNAMIC BOOKSHELF (Level 3)
 * * Concept: char ** (Pointer to Pointer)
 * - shelf: Là con trỏ trỏ tới mảng các con trỏ (char*)
 * - shelf[i]: Là con trỏ trỏ tới chuỗi ký tự thực tế
 * * Quy trình bộ nhớ:
 * 1. Malloc cái khung kệ sách (mảng các con trỏ).
 * 2. Malloc từng cuốn sách (mảng các ký tự).
 * 3. Free từng cuốn sách.
 * 4. Free cái khung kệ sách.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n;

    // 1. Nhập số lượng sách (Quyết định độ lớn của cái kệ)
    printf("May muon nhap bao nhieu cuon sach? (n): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Nhap so luong sai roi!\n");
        return 1;
    }
    
    // Xóa bộ nhớ đệm bàn phím sau khi nhập số để tránh trôi lệnh fgets
    int c;
    while ((c = getchar()) != '\n' && c != EOF);

    // 2. Cấp phát động cho CÁI KỆ (Mảng chứa n con trỏ char*)
    // Đây chính là char **
    char **shelf = (char**)malloc(n * sizeof(char*));
    
    // Rule #2: Luôn check NULL
    if (shelf == NULL) {
        fprintf(stderr, "Loi: Khong du RAM de xay ke sach!\n");
        return 1;
    }

    // 3. Nhập liệu từng cuốn
    printf("\n--- Bat dau xep sach len ke ---\n");
    for (int i = 0; i < n; i++) {
        char buffer[100]; // Biến tạm trên Stack
        printf("Ten sach so %d: ", i + 1);
        
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) break;
        buffer[strcspn(buffer, "\n")] = 0; // Xóa \n

        // Cấp phát động cho TỪNG CUỐN SÁCH
        shelf[i] = (char*)malloc(strlen(buffer) + 1);
        
        if (shelf[i] == NULL) {
            fprintf(stderr, "Loi: Het bo nho khi dang them sach thu %d!\n", i+1);
            // ROLLBACK: Dọn dẹp đống rác đã bày ra trước khi thoát
            for (int j = 0; j < i; j++) free(shelf[j]);
            free(shelf);
            return 1;
        }

        strcpy(shelf[i], buffer);
    }

    // 4. Xử lý logic (Tìm tên dài nhất)
    int max_len = 0;
    int idx_max = -1;

    printf("\n--- Review ke sach ---\n");
    for (int i = 0; i < n; i++) {
        printf("[%d] %s\n", i + 1, shelf[i]);
        
        int len = strlen(shelf[i]);
        if (len > max_len) {
            max_len = len;
            idx_max = i;
        }
    }

    if (idx_max != -1) {
        printf("\n=> Cuon day nhat la: \"%s\"\n", shelf[idx_max]);
    }

    // 5. DỌN DẸP (CLEANUP) - QUAN TRỌNG NHẤT
    // Nguyên tắc: Phá nhà từ trong ra ngoài.
    
    // Bước 5a: Trả lại từng cuốn sách (từng dòng dữ liệu)
    for (int i = 0; i < n; i++) {
        free(shelf[i]); 
    }

    // Bước 5b: Trả lại cái khung kệ sách
    free(shelf);
    shelf = NULL; // Thói quen tốt

    return 0;
}