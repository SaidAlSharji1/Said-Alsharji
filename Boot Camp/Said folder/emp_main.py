from exercise1_emp import Emloyee
def main():
    emp1 = Emloyee(123456 ,"Said" ,1500 ,"IT")
    emp1.print_employee_details()
    emp1.emp_assign_department("eng")
    emp1.print_employee_details()
    emp1.calculate_emp_salary(1500, 52)
    emp1.print_employee_details()





main()