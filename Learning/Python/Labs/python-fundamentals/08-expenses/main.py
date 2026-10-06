# Exercise: Expense Tracker
#
# Add several expenses and calculate the total.
#
# Concepts:
# - Lists
# - Loops
# - User input
# - Built-in functions

# Ask the user for each expense and store the values in a list.
total = 0
expenses = []
num_expenses = int(input("How many expenses do you want to enter?"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

# Calculate the total and show it to the user.
total = sum(expenses)
print("Total expenses are: $", total, sep="")
