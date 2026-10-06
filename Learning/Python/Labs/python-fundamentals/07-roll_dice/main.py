# Exercise: Roll the Dice
#
# Guess the result of a random dice roll.
#
# Concepts:
# - Imports
# - Random numbers
# - User input
# - Conditional logic

import random

# Generate a random die roll and ask the user to guess it.
roll = random.randint(1,6)
guess = int(input("Guess the dice roll :\n'"))

# Check whether the guess matches the roll.
if guess == roll:
    print("Correct! the computer rolled a " + str(roll))
else:
    print("Wrong! the computer rolled a " + str(roll))