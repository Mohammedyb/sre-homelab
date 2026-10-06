# Exercise: Age Calculator
#
# Break a user's age into decades and remaining years.
#
# Concepts:
# - User input
# - Type conversion
# - Integer division
# - Modulus
# - String concatenation

# Convert the input to an integer and separate the age into decades and years.
age = int(input("how old are you?\n"))
decades = age // 10
years = age % 10

# Display the result in a friendly format.
print("You are " + str(decades) + " decades and " + str(years) + " years old.")