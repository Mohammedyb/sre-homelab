# Exercise: Rock, Paper, Scissors
#
# Simulate a basic game against the computer using random choices.
#
# Concepts:
# - Imports
# - Randomness
# - User input
# - Conditional logic

import random

# Pick a random move for the computer and ask the user for theirs.
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('do you want to choose rock, paper, or scissors? ')

print("Computer chose: ", computer_choice)

# Compare both choices and decide the winner.
if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win!")
else:
    print("You lose!")
