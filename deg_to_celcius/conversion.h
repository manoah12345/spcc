// conversion.h

// Metre <-> Feet
#define METRE_TO_FEET(m) ((m) * 3.28084)
#define FEET_TO_METRE(f) ((f) / 3.28084)

// Litre <-> Cubic Feet
#define LITRE_TO_CUBIC_FEET(l) ((l) * 0.0353147)
#define CUBIC_FEET_TO_LITRE(cf) ((cf) / 0.0353147)

// Celsius <-> Fahrenheit
#define CELSIUS_TO_FAHRENHEIT(c) (((c) * 9.0 / 5.0) + 32)
#define FAHRENHEIT_TO_CELSIUS(f) (((f) - 32) * 5.0 / 9.0)
