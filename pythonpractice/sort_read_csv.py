students=[]
with open("names.csv") as csv_file:
    for line in csv_file:
        name,house=line.rstrip().split(",")
        student={"name":name,"house":house}
        students.append(student)
    
def get_name(student):
    return student["name"]

# for student in sorted(students,key=get_name):
#     print(f"{student['name']} lives in {student['house']}")
    
#alternate approach

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} lives in {student['house']}")
