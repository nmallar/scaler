class Parent:
    def __init__(self,name:str) -> None:
        self._name=name
    def printName(self):
        print("Inside parent class print method")
        print(self._name)
        
        
        
class Child(Parent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
    def printName(self):
        print("Inside child class print method")
        super().printName()
        print("Hey :- ",self._name)

def main():
    p=Parent("Parent")
    p.printName()
    c=Child("Child")
    c.printName()


if __name__=="__main__":
    main()