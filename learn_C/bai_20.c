/*Đề bài:
Viết chương trình nhập vào n (số lượng tên người). 
Sau đó nhập từng tên. Lưu trữ tất cả vào một mảng động char **. 
Cuối cùng in ra và free bộ nhớ.*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(void) 
{
    int n;
    printf("nhap so luong phan tu trong mang: "); scanf("%d",&n);
    char **names = (char**)malloc(n * sizeof(char*));
    int i;
    for(i=0 ; i<n ;i++)
    {
        char buffer[100];
        printf("nhap ten: "), scanf("%s", &buffer);
        names[i] = (char*)malloc(strlen(buffer) + 1); //+1 cho ký tự \0 kết thúc chuỗi
        strcpy(names[i], buffer);
    }
    printf("danh sach: ");
    for (i=0;i<n;i++)
    {
        printf("%s ",names[i]);
        free(names[i]);
    }
    free(names);
    return 0;
}
