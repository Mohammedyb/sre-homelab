from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, firstname, lastname, weekly_hours, hourly_rate):
        super().__init__(firstname, lastname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate


    def calculate_paycheck(self):
        return self.weekly_hours * self.weekly_hours