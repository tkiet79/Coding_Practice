#include<stdio.h>
#define PI 3.1415

int main(void) {
    float r, C, S;
    printf("enter radian: ");
    scanf("%f", &r);
    C = 2 * PI * r;
    S = PI * r * r;

    printf("chu vi hinh tron la: %.2f", C);
    printf("\ndien tich hinh tron la: %.2f", S);
    return 0;
}