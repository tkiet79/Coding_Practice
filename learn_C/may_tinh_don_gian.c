#include<stdio.h>

int main(void) {
    long a, b;
    long res;
    printf("enter value of a and b: ");
    scanf("%ld%ld", &a, &b);

    char op;
    printf("enter your operation: ");

    scanf(" %c", &op);

    switch (op)
    {
    case '+':
        res = a + b;
        printf("ket qua la: %ld", res);
        break;
    
    case '-':
        res = a - b;
        printf("ket qua la: %ld", res);
        break;

    case '*':
        res = a * b;
        printf("ket qua la: %ld", res);
        break;
    
    case '/':
        if (b == 0) {
            printf("khong the chia cho 0 !!!");
        } else {
        res = a / b;
        printf("ket qua la: %ld", res);
        break;
        }
    }
}