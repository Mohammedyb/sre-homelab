# Exercise: Greetings
#
# Print a greeting to the user using a simple function.
#
# Concepts:
# - Functions
# - Variables
# - User input
# - Output

# Define a function that prints a greeting using the global name variable.
def greeting():
    print("Hello", name)

# Collect the user name and call the greeting function.
name = input("Enter your name:\n")
greeting()