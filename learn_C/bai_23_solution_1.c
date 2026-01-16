/*Bài 3: Tủ sách cố định (Static Array of Dynamic Strings) - Level 2.5

Mục tiêu: Bước đệm để hiểu char **. Ở đây ta dùng mảng con trỏ cố định kích thước.

Bối cảnh:
Mày có một cái kệ sách có đúng 5 ngăn (char *shelf[5]). Mỗi ngăn sẽ chứa tên một cuốn sách, nhưng độ dài tên sách thì khác nhau.

Yêu cầu:

1. Khai báo char *shelf[5]; (Đây là mảng chứa 5 con trỏ char*, nằm trên Stack).
2. Dùng vòng lặp nhập tên 5 cuốn sách:
4. Dùng buffer tạm để đọc tên sách.
4. Dùng malloc (hoặc hàm my_strdup ở bài 2) để cấp phát bộ nhớ vừa khít cho tên sách.
5. Lưu địa chỉ đó vào shelf[i].
6. In danh sách các cuốn sách.
7. Tìm và in ra cuốn sách có tên dài nhất.
8. Dọn dẹp: Dùng vòng lặp free từng shelf[i]. (Lưu ý: Không cần free(shelf) vì shelf là mảng tĩnh).*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(void)
{
    char *shelf[5];
    for (int i = 0; i < 5; i++)
    {
        char buffer[100];
        printf("nhap ten sach: ");
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            break;
        }
        buffer[strcspn(buffer, "\n")] = 0;
        shelf[i] = (char*)malloc(strlen(buffer) + 1); //+1 cho ký tự \0 kết thúc chuỗi

        if (shelf[i] == NULL) {
            fprintf(stderr, "Loi: Khong du bo nho!\n");
            // Xử lý dọn dẹp những cái đã cấp phát trước đó nếu cần kỹ tính
            return 1;
        } 
        strcpy(shelf[i], buffer);
    }

    int max_len = 0;
    int index_max = 0;
    for (int i = 0; i < 5; i++) {
        printf("- %s\n", shelf[i]);
        
        // Logic tìm max
        int current_len = strlen(shelf[i]); // Dùng strlen, KHÔNG dùng sizeof
        if (current_len > max_len) {
            max_len = current_len;
            index_max = i; // Lưu lại vị trí (index) an toàn hơn lưu con trỏ tạm
        }
    }
    printf("\n=> Cuon sach co ten dai nhat la: \"%s\" (Dai %d ky tu)\n", shelf[index_max], max_len);
    for (int i = 0; i < 5; i++) {
        free(shelf[i]);
        shelf[i] = NULL; // Thói quen tốt
    }

    return 0;
}