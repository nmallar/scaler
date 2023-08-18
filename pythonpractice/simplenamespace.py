

# use simplenamespace when you want to create a custom class without any functions/methods in it but only instance variables


def square(instance):
    instance.n *= instance.n 

from types import SimpleNamespace

ns=SimpleNamespace()
ns.n=4
print(f"before squre(ns)",ns.n)
square(ns)

print(f"after squre(ns)",ns.n)