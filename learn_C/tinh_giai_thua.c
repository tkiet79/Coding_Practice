#include<stdio.h>

int fac(int); 

int main()
{
    int n;
    printf("nhap 1 so bat ky: ");
    scanf("%d", &n);
    int res = fac(n);
    printf("giai thua cua n la: %d", res);
    return 0;
}

int fac(int n) 
{
    if (n<=1) {
        return 1;
    } else {
        return fac(n-1) * n;
    }

}