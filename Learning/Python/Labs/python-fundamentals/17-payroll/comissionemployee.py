# Exercise: Commission Employee
#
# Create a payroll employee whose pay includes a base salary plus commission.
#
# Concepts:
# - Inheritance
# - Method overriding
# - Instance attributes
# - Calculation logic

from salaryemployee import SalaryEmployee


# Commission employees earn their base salary plus extra commission on sales.
class ComissionEmployee(SalaryEmployee):
    def __init__(self, firstname, lastname, salary, sales_num, com_rate):
        super().__init__(firstname, lastname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num * self.com_rate
        return regular_salary + total_commission