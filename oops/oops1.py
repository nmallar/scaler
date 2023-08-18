class Person:
    description="General person"
    
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}")
    
    def eat(self,food):
        print(f"{self.name } eats {food}")
        
    def action(self):
        print(f"{self.name} spins")
        
class Baby(Person):
    description="baby"
    
    def speak(self):
        print(f" ba  ba  ba")
    def nap(self):
        print(f"{self.name} takes a nap")
        
person=Person("Steve",20)
person.speak()
person.eat("pizza")
person.action()

baby=Baby("Amit",1)
baby.speak()
baby.eat("cerelac")
baby.action()

print(person.description)
print(baby.description)

print(isinstance(baby,object))