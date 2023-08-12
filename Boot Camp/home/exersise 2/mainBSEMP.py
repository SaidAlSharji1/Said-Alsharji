import pandas as pd
from BinarySearchEmp import Employee
#assuming alreadt have data into  exel file into a datafram d
df = pd.read_excel("Reading.xlsx", sheet_name = "Sample")
print("%-20s%-20s%-10s"%("Name","Id","Salary"))
print("-"*50)
pList = []
for index, row in df.iterrows(): # it will display every row
    eName = row['Name']
    eId = row['Id']
    eSalary = row['Salary']
    currentemp = Employee(eName, eId, eSalary)
    pList.append(currentemp)

    print("%-20s%-20s%-10.1f"%(eName, eId,eSalary))

#outside the loop
print(len(pList))



for p in pList:
    print("%-20s%-20s%-10.1f"%(p.get_name(),p.get_id(),p.get_eSalary()))

nList=[]
n=0
for p in pList:
    
    if p.get_id() >= n:
        nList.append(p)
        n= p.get_id()
        print(n)
    else:
        nList.insert(0,p)


for p in nList:
    print("%-20s%-20s%-10.1f"%(p.get_name(),p.get_id(),p.get_eSalary()))
    
      
    


# from BinarySearchEmp import Employee  
# def main():
#     x=Employee.read_emp_file('Reading.xlsx')
#     for i in x:
#         print (i)
#     Employee.printAll()
# main()