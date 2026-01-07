#include<stdio.h>

int main(void) 
{
    int n;
    printf("nhap 1 so bat ky: ");
    scanf("%d", &n);
    int i;
    for (i=1;i<=10;i++) 
    {
        int res = i * n;
        printf("\n%d x %d = %d", n, i, res);
    }
    return 0;
}