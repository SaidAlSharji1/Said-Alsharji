import csv

csv_data = []
list1 = []
t=0
sumx=0
with open('fileCsv.csv', 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)  # Use DictReader to create dictionaries for rows
    for row in csvreader:
        csv_data.append(row)  # Append the dictionary to the list
        print(row)
        print(csv_data)
    for item  in range (len(csv_data)):
        print(csv_data[item]['GPA'])
        list1.append(float(csv_data[item]['GPA']))
        
    sumx = sum(list1)
    t = len(list1)
    avg = sumx / t    
    print( "Avrage = " ,avg)
    h=int(input("how many student you want to add: "))
    for i in range(h):  
        ida=input("plase enter the id of student: ")
        nName=input("plase enter the name of student: ")
        nGpa=input("plase enter the GPA of student: ")
        n= int(input("Plase choose the place you want to add the data of student: "))
         # Insert the new data at the desired row
        newd= {}
        newd['Id']=ida
        newd['Name']=nName
        newd['GPA']=nGpa
        csv_data.insert(n-1,newd)
        list1.insert(n-1,nGpa)
              

        print("Data inserted successfully.")
    print("The updated list ",list1)
    
  
