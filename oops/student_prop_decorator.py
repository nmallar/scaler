#property decorator

class Student:
    def __init__(self,id) -> None:
        self.__id=id
        
        
    @property
    def id(self):
        print('Getting id to')
        return self.__id


    #setter method
    @id.setter
    def id(self,val):
        print('Setting id to ', val)
        self.__id=val
    
def main():
    
    student=Student('John')
    print(student.id)
    student.id='James'
    print(student.id)
    
if __name__=="__main__":
    main()
  