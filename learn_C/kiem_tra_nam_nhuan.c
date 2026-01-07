#include<stdio.h>

int main(void) {
    int year;
    printf("enter your year: ");
    scanf("%d", &year);

    if (year % 400 == 0 || year % 4 == 0 && year % 100 != 0) {
        printf("%d la nam nhuan", year);
    } else {
        printf("%d khong phai nam nhuan", year);
    }
    
}
