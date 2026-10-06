# Exercise: Addition
#
# Add two numbers together using a reusable function.
#
# Concepts:
# - Functions
# - Parameters
# - Return values
# - User input
# - Type conversion

# Define a function that adds two values and returns the result.
def addition(a, b):
    return a + b

# Run the main program and use the function to calculate the answer.
def main():
    num1 = float(input("Enter your 1st number:\n"))
    num2 = float(input("Enter your 2nd number:\n"))

    result = addition(num1, num2)
    print("The result is", result)

main()