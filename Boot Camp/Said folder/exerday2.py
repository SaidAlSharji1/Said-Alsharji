import pandas as pd
import openpyxl

class Emloyee:
    def __init__(self,   emp_name, emp_id , emp_salary ):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        df = pd.DataFrame([emp_name, emp_id, emp_salary],
                  index=['one', 'two', 'three'], columns=['name', 'id', 'salary'])
        df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

        print(df)
    
     
        
    def emp_assign_department(self, newDepartment):
        self.emp_department = newDepartment
    def print_employee_details(self):
        print(f"employee name {self.emp_name}")
        print(f"employee id is {self.emp_id}")
        print(f"employee salary = {self.emp_salary}")
        print(f"employee department is {self.emp_department}")
            


