class Employee:
    def __init__(self, eName, eId,eSalary ):
        self.eName = eName
        self.eId = eId
        self.eSalary = eSalary
#         
#     def read_emp_file(file):
#         Employees = []
#         
#         op = openpyxl.load_workbook(file)
#         sheet = op.active
#         
#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             eName, eId , eSalary = row
#             Employees.append(Employee(eName, eId, eSalary))
#        
#         return Employees


    def get_id(self):
        return self.eId
    def get_name(self):
        return self.eName
    def get_eSalary(self):
        return self.eSalary
    
    def set_eId(self, newId):
        self.eId = newId
    def set_eName(self, newn):
        self.eName = newn
    def set_eSalary(self, newS):
        self.eSalary = newS
        
    def binary_search_employees(employee_list, target_id):
        left, right = 0, len(employee_list) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if employee_list[mid].emp_id == target_id:
                return employee_list[mid]
            elif employee_list[mid].emp_id < target_id:
                left = mid + 1
            else:
                right = mid - 1

        return None
    
#     def empBS(arr, target):
#          left, right = 0, len(arr) - 1
# 
#     while left <= right:
#         mid = (left + right) // 2
# 
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# 
#     return -1

    
     

        
    
  



        