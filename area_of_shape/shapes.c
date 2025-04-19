#include <stdio.h>
#define AREA_CIRCLE(r) (3.1415 * (r) * (r))
#define AREA_RECTANGLE(l, b) ((l) * (b))
#define AREA_SQUARE(s) ((s) * (s))
#define AREA_TRIANGLE(b, h) (0.5 * (b) * (h))


int main() {
    float radius , length , breadth , side , base , height ;

    printf("enter the radius:\n");
    scanf("%f",&radius);
    printf("Area of Circle: %.2f\n", AREA_CIRCLE(radius));

    printf("enter the length and Breadth:\n");
    scanf("%f %f",&length,&breadth);
    printf("Area of Rectangle: %.2f\n", AREA_RECTANGLE(length, breadth));

    printf("enter the side:\n");
    scanf("%f",&side);
    printf("Area of Square: %.2f\n", AREA_SQUARE(side));

    printf("Enter the base and height of the triangle:\n");
    if (scanf("%f %f", &base, &height) != 2 || base <= 0 || height <= 0) {
        printf("Invalid input for base and height. Please enter positive numbers.\n");
        return 1; // Exit the program if invalid input
    }
    printf("Area of Triangle: %.2f\n", AREA_TRIANGLE(base, height));

    printf("\nPress Enter to exit...");
    getchar(); // To consume any newline character from previous input
    getchar(); 

    return 0;
} 