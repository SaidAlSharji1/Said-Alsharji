class Emloyee:
    def __init__(self, emp_id , emp_name , emp_salary , emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary/50))
            self.emp_salary =  self.emp_salary + overtime_amount
            print(f"the salary = {self.emp_salary}")
        else:
             self.emp_salary = salary
             print(f"the salary = {self.emp_salary}")   
        
    def emp_assign_department(self, newDepartment):
        self.emp_department = newDepartment
    def print_employee_details(self):
        print(f"employee name {self.emp_name}")
        print(f"employee id is {self.emp_id}")
        print(f"employee salary = {self.emp_salary}")
        print(f"employee department is {self.emp_department}")
            