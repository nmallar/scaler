import copy


def deepcopy(obj):
    if isinstance(obj, dict):
        return {deepcopy(key): deepcopy(value) for key, value in obj.items()}
    if hasattr(obj, '__iter__'):
        return type(obj)(deepcopy(item) for item in obj)
    return obj


dict1={'a':1,'b':2,'c':3,'d':{'e':5,'f':6},'g':7,'h':{'i':9},'j':10}
#dict1={'a':1,'b':2,'c':3,'g':7,'j':10}

dict2=dict1

print("dict1 id ",id(dict1))
print("dict2 id",id(dict2))

dict1['a']=22

print("dict1[a]",dict1['a'])
print("dict2[a]",dict2['a'])



dict3=deepcopy(dict1)

dict1['a']=99

dict3['a']=188

print("dict1 id ",id(dict1))
print("dict2 id",id(dict2))
print("dict3 id",id(dict3))
print("dict1[a]",dict1['a'])
print("dict2[a]",dict2['a'])
print("dict3[a]",dict3['a'])
for key,value in dict3.items():
    print(key,value)