# Exercise: Loan Calculator
#
# Model a loan and track how each monthly payment reduces the balance.
#
# Concepts:
# - User input
# - Loops
# - Conditional logic
# - Interest calculations
# - Break statements

# Get the loan details needed to calculate monthly payments.
money_owed = float(input("How much money do you owe, in dollars? \n"))
apr = float(input("what is the annual percentage rate of the loan?\n"))
payment = float(input("How much will you pay off each month in dollars?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthly_rate = apr/100/12

# Simulate each month and stop once the loan is paid off.
for i in range(months):
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i*1, "months")
        break

    money_owed = money_owed - payment
    print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now I owe", money_owed)

