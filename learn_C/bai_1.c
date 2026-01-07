#include <stdio.h>
float convert(float);
int main() {
    printf("Enter Your temperture C: ") ;
    float C;

    scanf("%f", &C);
    float F = convert(C);
    printf("convert temperture C --> F is: %.2f F temperture",F);
    return 0;

}

float convert(float C) {
    return (1.8 * C) + 32;
}