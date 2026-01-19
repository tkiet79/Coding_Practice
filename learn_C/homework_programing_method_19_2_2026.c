// kiểm tra số nguyên tố từ 1 --> n
#include<stdio.h>
#include <stdbool.h>
bool is_prime(long long n);
int main()
{
    long long n;
    printf("nhap 1 so bat ky: "); scanf("%lld",&n);
    if (is_prime(n))
    {
        printf("%lld la so nguyen to", n);
    }
    else
    {
        printf("%lld khong phai so nguyen to", n);
    }
    return 0;
}

bool is_prime(long long n) {
    // 1. Base cases (Trường hợp cơ bản)
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (long long i = 3; i * i <= n; i += 2) {
        if (n % i == 0 ) return false;
    }

    return true;
}
