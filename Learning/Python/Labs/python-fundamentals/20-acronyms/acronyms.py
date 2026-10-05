
from pathlib import Path

ACRONYMS_FILE = Path(__file__).with_name("acronyms.txt")


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
    except FileNotFoundError as e:
        print("File not Found") 
        return           

    if not found:
        print("The acronym does not exist")        

def add_acronyms(): 
     # ask user what acronym they want to add
     acronym = input("What acronym do you want to add? \n")
    # ask the user for the definition
     definition = input ("what is the definition?\n")
    #open the file 
     with open(ACRONYMS_FILE, 'a') as file:
        
        #write the acronym to the new file 
        file.write(acronym + " - " + definition + '\n')

def main():
    #ask the user if they want to find or add acronym
    choice = input("Do you want to find(F) or add (A) \n")
    if choice == 'F':
        find_acronyms()
    elif choice == 'A':
        add_acronyms()

main()            