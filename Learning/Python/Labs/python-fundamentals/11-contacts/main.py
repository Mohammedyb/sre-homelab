# Exercise: Contacts
#
# Store a list of student records in a dictionary and print only their emails.
#
# Concepts:
# - Dictionaries
# - Nested data structures
# - Loops
# - Indexing

# Create a dictionary that holds the total number of students and each student record.
contacts = {
    "number": 4,
    "students": [
        {"name": "Mohammed Bubshait", "email": "mohammed@example.com"},
        {"name": "Bianca Chanel", "email": "Bianca@example.com"},
        {"name": "Ibrahim Mohammed", "email": "Ibrahim@example.com"},
        {"name": "Abdulaziz Mohammed", "email": "Abdulaziz@example.com"},
    ]
}

# Print only the email address for each student.
print("Sudent emails:")
for student in contacts['students']:
    print(student["email"])
