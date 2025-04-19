#include <stdio.h>

#define FIBONACCI_SERIES(n) fibonacciSeries(n)
#define PRIME_SERIES(n) primeSeries(n)
#define LEAP_YEAR_SERIES(start, end) leapYearSeries(start, end)

// Function to generate Fibonacci Series
void fibonacciSeries(int n) {
    int t1 = 0, t2 = 1, nextTerm;
    printf("\nFibonacci Series up to %d terms:\n", n);
    for (int i = 1; i <= n; ++i) {
        printf("%d ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    printf("\n");
}

// Function to generate Prime Numbers up to n
void primeSeries(int n) {
    int i, j, flag;
    printf("\nPrime Numbers up to %d:\n", n);
    for (i = 2; i <= n; i++) {
        flag = 0;
        for (j = 2; j <= i/2; j++) {
            if (i % j == 0) {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
            printf("%d ", i);
    }
    printf("\n");
}

// Function to generate Leap Years between start and end
void leapYearSeries(int start, int end) {
    printf("\nLeap Years between %d and %d:\n", start, end);
    for (int year = start; year <= end; year++) {
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
            printf("%d ", year);
    }
    printf("\n");
}

int main() {
    int n, start, end;

    printf("Enter number of terms for Fibonacci Series: ");
    scanf("%d", &n);
    FIBONACCI_SERIES(n);

    printf("\nEnter upper limit for Prime Numbers: ");
    scanf("%d", &n);
    PRIME_SERIES(n);

    printf("\nEnter start and end year for Leap Years: ");
    scanf("%d %d", &start, &end);
    LEAP_YEAR_SERIES(start, end);

    return 0;
}
