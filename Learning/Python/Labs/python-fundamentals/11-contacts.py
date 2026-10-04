# Create Dictionary of Contacts, with the key number for amount of students
## Create Key students with list as the value
### Inside the list are dictionaries with each students information
contacts = {
    "number" : 4,
    "students":
        [
            {"name": "Mohammed Bubshait" , "email":"mohammed@example.com"},
            {"name": "Bianca Chanel" , "email":"Bianca@example.com"},
            {"name": "Ibrahim Mohammed" , "email":"Ibrahim@example.com"},
            {"name": "Abdulaziz Mohammed" , "email":"Abdulaziz@example.com"},
                
        ]
} 

# Only print out list of emails to make emails list
print("Sudent emails:")
for student in contacts['students']:
    print(student["email"])
