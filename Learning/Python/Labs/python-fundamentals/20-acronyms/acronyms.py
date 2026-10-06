# Exercise: Acronym Lookup
#
# Search for common software acronyms or add a new one to a local dictionary file.
#
# Concepts:
# - File handling
# - `pathlib`
# - User input
# - Conditionals
# - Basic persistence

from pathlib import Path

ACRONYMS_FILE = Path(__file__).with_name("software_acronyms.txt")


# Look up an acronym in the saved lookup file.
def find_acronyms():
    look_up = input("What software acronym would you like to look up? \n")

    found = False
    try:
        with open(ACRONYMS_FILE) as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError:
        print("File not Found")
        return

    if not found:
        print("The acronym does not exist")


# Add a new acronym and definition to the file.
def add_acronyms():
    acronym = input("What acronym do you want to add? \n")
    definition = input("what is the definition?\n")

    with open(ACRONYMS_FILE, 'a') as file:
        file.write(acronym + " - " + definition + '\n')


# Let the user choose whether to search or append an acronym.
def main():
    choice = input("Do you want to find(F) or add (A) \n")
    if choice == 'F':
        find_acronyms()
    elif choice == 'A':
        add_acronyms()

main()