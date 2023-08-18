from random import choice
class Pet:
    def __new__(cls):
        other=choice([Dog,Cat,Python])
        instance=super().__new__(other)
        print(f"I am a {type(instance).__name__}")
        return instance
    
    def __init__(self):
        print("Never runs!")
        
class Dog:    
    def say(self):
        print("woof woof!")
class Cat:    
    def say(self):
        print("Meow Meow!")
class Python:    
    def say(self):
        print("hiss hiss!")
 