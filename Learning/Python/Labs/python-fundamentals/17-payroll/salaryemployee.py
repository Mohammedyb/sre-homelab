from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52