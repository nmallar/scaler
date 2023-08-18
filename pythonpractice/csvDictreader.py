import csv
students=[]

try:
    with open("names_with_header.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            
            students.append({"name":row['name'],"home":row['home'],"city":row['city']})
   
        for student in sorted(students,key=lambda student:student['name']):
            print (f"{student['name']} lives in {student['city']}")



except  FileNotFoundError:
    print("File not found")