import sys,gc
a=10
b=10
del b
print(sys.getrefcount(a))
print(id(a))
print(gc.collect())