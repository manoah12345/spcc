def generate_three_address_code(a, b, c, d):
    # Step 1: Compute a + b
    t1 = a + b
    print(f"t1 = {a} + {b}")

    # Step 2: Compute c - d
    t2 = c - d
    print(f"t2 = {c} - {d}")

    # Step 3: Multiply the results and assign to x
    x = t1 * t2
    print(f"x = t1 * t2")
    
    return x

# Example usage:
a, b, c, d = 5, 3, 8, 2  # Example values for a, b, c, d
result = generate_three_address_code(a, b, c, d)
print(f"Result of x: {result}")
