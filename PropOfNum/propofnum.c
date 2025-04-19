#include <stdio.h>

#define FACTORIAL(n) factorial(n)
#define SUM_NATURAL(n) ((n) * ((n) + 1) / 2)

// Function to calculate factorial
long long int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d: %lld\n", n, FACTORIAL(n));
    }

    printf("Sum of natural numbers till %d: %d\n", n, SUM_NATURAL(n));

    return 0;
}
