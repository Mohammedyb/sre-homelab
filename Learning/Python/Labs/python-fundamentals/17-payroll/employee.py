# Exercise: Employee Base Class
#
# Define the shared employee data used by the payroll example.
#
# Concepts:
# - Classes
# - Attributes
# - Inheritance

# Base class for employee records shared by all payroll subclasses.
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
