#include<stdio.h>

int main(void) {
    double a,b,c;
    printf("nhap 3 gia tri cho a, b, c: ");
    scanf("%lf%lf%lf", &a, &b, &c);

    if (a + b > c && a + c > b && b + c > a) {
        printf("%.2lf, %.2lf, %.2lf co the tao thanh tam giac", a, b, c);
    } else {
        printf("%.2lf, %.2lf, %.2lf khong the tao thanh tam giac", a, b, c);
    }
}