from employee import Employee

class Company:
    def __init__(self):
        self.employees =[]

    def add_emplyoee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.firstname, i.lastname)

    def pay_employees(self):
        print("Paying Employees: ")
        for i in self.employees:
            print("paycheck for:", i.firstname, i.lastname)
            print(f"Amount: ${i.calculate_paycheck():,.2f}")
            print("------------------------------")

def main():
    my_company = Company()

    employee1 = Employee('Mohammed','Bubshait', 100000)
    my_company.add_emplyoee(employee1)   
    
    employee2 = Employee('Bianca','Bubshait', 200000)
    my_company.add_emplyoee(employee2)
    
    employee3 = Employee('Ibrahim','Bubshait', 50000)
    my_company.add_emplyoee(employee3)
    
    employee4 = Employee('Abdulaziz','Bubshait', 25000)
    my_company.add_emplyoee(employee4)

    my_company.display_employees()
    my_company.pay_employees()

main()