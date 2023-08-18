import csv

students=[]
try:
    with open("names.csv") as csv_file:
        reader=csv.reader(csv_file)
        for name,home in reader:
            students.append({"name":name,"home":home})
        
        
        for student in sorted(students , key =lambda student: student['name']):
            print(f"{student['name']} stays in {student['home']}")
except FileNotFoundError:
    print(f"File not found")
    