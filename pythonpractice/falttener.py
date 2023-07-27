

my_list=[1,2,3,[4,5],[[5,6],7],[8,9,0]]

def flattener(lst):
    result=[]
    while lst:
        item=lst.pop()
        if type(item)==list:
            lst.extend(item)
        else:
            result.append(item)
    return result[::-1]

print(flattener(my_list))  