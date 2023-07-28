class Student:
    def __init__(self) -> None:
        print("Inside default constructor")
        self.name="John"
        self.age=25
        
    # def __init__(self,name):
    #     print("Inside parameterized constructor")
    #     self.name=name
        
    def print_name(self):
        print(self.name)

    def __del__(self):
        print("Destructor called")
        
def main():
    student_object=Student()
    student_object.print_name()
    # student_object2=Student("Ashok")
    # student_object2.print_name()
    del student_object
    
    
if __name__=="__main__":
    main()