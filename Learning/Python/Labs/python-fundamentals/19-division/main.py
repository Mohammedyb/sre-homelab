# Exercise: Division with Remainder
#
# Explore integer division and remainder handling with a guard for zero divisors.
#
# Concepts:
# - Functions
# - Arithmetic operators
# - Exceptions
# - Division and modulus

# Divide two numbers and print both the quotient and remainder.
def remainder_division(a, b):
    if b == 0:
        raise Exception("Divisor cannot be 0")
    result = a // b
    remainder = a % b
    print(a, "/", b, "is", result, "remainder", remainder)

# Run the example against a zero divisor to show the exception.
remainder_division(10, 0)
