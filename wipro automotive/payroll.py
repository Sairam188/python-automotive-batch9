class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_net_salary(self):
        try:
            return self.basic_salary + self.calculate_hra() + self.calculate_da()
        except:
            return 0


# taking inputs
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# creating object
emp = Employee(emp_id, name, basic_salary)

# displaying result
print("Employee ID:", emp.emp_id)
print("Employee Name:", emp.name)
print("Net Salary:", emp.calculate_net_salary())
