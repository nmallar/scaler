class Student:
    def __init__(self, name:str,batchId:int,universityName:str) -> None:
        self._name=name
        self.__batchId=batchId
        self.universityName=universityName
        
    def changeBatch(self,newBatchId:int):
        self.batchId=newBatchId

class StudentChild(Student):
    def __init__(self)->None:
        #super().__init__(name,batchId,universityName)
        super().__init__("Amar",1,"MIT")
        print("We are inside childclass constructor")
        print(self._name)
        print(self._Student__batchId)

def main():
    student=Student(name="James",batchId=3,universityName="MIT")
    print(student._name)
    print("Before changing batch id",student._Student__batchId)    
    student.changeBatch(newBatchId=4)
    print("after changing batch id :" ,student._Student__batchId)
    studentch=StudentChild()
    print(studentch._name)
    print(studentch._Student__batchId)
    

if __name__=="__main__":
    
    main()
   