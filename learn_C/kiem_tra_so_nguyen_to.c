#include<stdio.h>
#include<math.h>

long is_prime(int);
long  main(void) {
    long  N;
    printf("Nhap 1 so nguyen bat ky: ");
    scanf("%d", &N);        
    int res = is_prime(N);
    if (res == 0) {
        printf("%d Khong phai so nguyen to ", N);
    } else if (res == 1) {
    printf("%d la So nguyen to ", N);    
}
    return 0;
}
long is_prime(int n) { 
    if (n < 1) {
        return 0;
    } else if (n == 2) {
        return 1;
    } else if (n % 2 == 0) {
        return 0;
    }
    long i;
    for (i=3;i<=pow(n,1/2);i= i + 2) {
        if (n % i == 0) {
            return 0;
        } 
    } 
    return 1;
}