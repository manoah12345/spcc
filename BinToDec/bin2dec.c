#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

// Macros for conversions
#define BINARY_TO_DECIMAL(bin) binaryToDecimal(bin)
#define DECIMAL_TO_BINARY(dec) decimalToBinary(dec)
#define BINARY_TO_HEX(bin) binaryToHex(bin)
#define HEX_TO_BINARY(hex) hexToBinary(hex)

int binaryToDecimal(long long bin) {
    int dec = 0, i = 0, rem;
    while (bin != 0) {
        rem = bin % 10;
        bin /= 10;
        dec += rem * pow(2, i);
        ++i;
    }
    return dec;
}

void decimalToBinary(int dec) {
    int bin[32], i = 0;
    while (dec > 0) {
        bin[i] = dec % 2;
        dec /= 2;
        i++;
    }
    printf("Binary: ");
    for (int j = i - 1; j >= 0; j--)
        printf("%d", bin[j]);
    printf("\n");
}

void binaryToHex(long long bin) {
    int dec = binaryToDecimal(bin);
    printf("Hexadecimal: %X\n", dec);
}

void hexToBinary(char hex[]) {
    int i;
    printf("Binary: ");
    for(i = 0; hex[i] != '\0'; i++) {
        switch(hex[i]) {
            case '0': printf("0000"); break;
            case '1': printf("0001"); break;
            case '2': printf("0010"); break;
            case '3': printf("0011"); break;
            case '4': printf("0100"); break;
            case '5': printf("0101"); break;
            case '6': printf("0110"); break;
            case '7': printf("0111"); break;
            case '8': printf("1000"); break;
            case '9': printf("1001"); break;
            case 'A': case 'a': printf("1010"); break;
            case 'B': case 'b': printf("1011"); break;
            case 'C': case 'c': printf("1100"); break;
            case 'D': case 'd': printf("1101"); break;
            case 'E': case 'e': printf("1110"); break;
            case 'F': case 'f': printf("1111"); break;
            default: printf("Invalid hexadecimal digit %c", hex[i]);
        }
    }
    printf("\n");
}

int main() {
    long long bin;
    int dec;
    char hex[20];

    printf("Enter a binary number: ");
    scanf("%lld", &bin);
    printf("Decimal: %d\n", BINARY_TO_DECIMAL(bin));
    BINARY_TO_HEX(bin);

    printf("\nEnter a decimal number: ");
    scanf("%d", &dec);
    DECIMAL_TO_BINARY(dec);

    printf("\nEnter a hexadecimal number: ");
    scanf("%s", hex);
    HEX_TO_BINARY(hex);

    return 0;
}
