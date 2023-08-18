class Dog:
    species='mammal'
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def description(self):
        return f"{self.name} is {self.age}"
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
    def birthday(self):
        self.age+=1

mikey=Dog("Mikey",6)

print(mikey.description()    )

print(mikey.speak("gruff gruff"))

mikey.birthday()

print(mikey.description())
