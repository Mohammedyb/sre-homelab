# Exercise: Hourly Employee
#
# Create a payroll employee whose pay is based on hours worked and hourly rate.
#
# Concepts:
# - Inheritance
# - Instance attributes
# - Methods

from employee import Employee


# Hourly employees are paid based on hours worked and their hourly rate.
class HourlyEmployee(Employee):
    def __init__(self, firstname, lastname, weekly_hours, hourly_rate):
        super().__init__(firstname, lastname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate