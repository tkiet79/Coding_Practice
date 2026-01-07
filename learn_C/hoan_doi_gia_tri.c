#include <stdio.h>

int main(void) {
    int a,b;
    int temp;
    printf("enter value of a and b: ");
    scanf("%d%d", &a, &b);
    temp = a;
    a = b;
    b = temp;
    printf("%d\n%d",a, b);
    return 0;
}