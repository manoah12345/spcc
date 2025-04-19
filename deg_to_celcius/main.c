#include <stdio.h>
#include "conversion.h" // Including your own library

int main() {
    float metre, feet, litre, cubic_feet, celsius, fahrenheit;

    // Meter to Feet
    printf("Enter metres: ");
    scanf("%f", &metre);
    printf("%.2f metres = %.2f feet\n", metre, METRE_TO_FEET(metre));

    // Feet to Meter
    printf("Enter feet: ");
    scanf("%f", &feet);
    printf("%.2f feet = %.2f metres\n", feet, FEET_TO_METRE(feet));

    // Litre to Cubic Feet
    printf("Enter litres: ");
    scanf("%f", &litre);
    printf("%.2f litres = %.2f cubic feet\n", litre, LITRE_TO_CUBIC_FEET(litre));

    // Cubic Feet to Litre
    printf("Enter cubic feet: ");
    scanf("%f", &cubic_feet);
    printf("%.2f cubic feet = %.2f litres\n", cubic_feet, CUBIC_FEET_TO_LITRE(cubic_feet));

    // Celsius to Fahrenheit
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    printf("%.2f°C = %.2f°F\n", celsius, CELSIUS_TO_FAHRENHEIT(celsius));

    // Fahrenheit to Celsius
    printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &fahrenheit);
    printf("%.2f°F = %.2f°C\n", fahrenheit, FAHRENHEIT_TO_CELSIUS(fahrenheit));

    return 0;
}
