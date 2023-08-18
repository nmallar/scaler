from dec import *

@do_twice
def sayhi():
    print("Hi!")
    

@do_twice
def sayHiName(name):
    print("Hi",name)
    return f"I said hi"

@timer
def waste_some_time(num):
    sum([i**2 for i in range(num)])

@debug
def add(num1,num2):
    return int(num1)+int(num2)