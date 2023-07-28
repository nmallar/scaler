class Student:
    def print_name(self,name):
        print(type(self))
        print(name)

studentobj=Student()
studentobj.print_name("Mailar")
Student.print_name(studentobj,"Mailar") # this is how python implicitly calls the above statement  studentobj.print_name("Mailar")