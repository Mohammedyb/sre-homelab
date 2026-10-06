# Exercise: Salary Employee
#
# Create a payroll employee whose pay is based on an annual salary.
#
# Concepts:
# - Inheritance
# - Class attributes
# - Methods

from employee import Employee


# Salary employees receive a paycheck based on the annual salary divided by 52 weeks.
class SalaryEmployee(Employee):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52