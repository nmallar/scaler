class Parent1:
    
    def doSomething(self):
        print("Called parent1")

class Parent2:
    def doSomething(self):
        print("Called Parent2")

class Child(Parent1,Parent2):
        def __init__(self) -> None:
             pass

class ChildSecond(Parent2, Parent1):
    pass

ch=Child()
ch.doSomething()    # invokes doSomething of Parent1 class as its the first parent class in inherited list

ch2=ChildSecond() 
ch2.doSomething() # invokes doSomething of Parent2 class as its the first parent class in inherited list