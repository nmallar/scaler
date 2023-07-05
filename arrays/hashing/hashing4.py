#hashing
#given an array of N elements check if all elements are distinct or not

A=[3,4,9,7]
print(f"Original array is {A}")


#dict approach
# dict={}
# unique=True
# for n in A:    
#     dict[n]=dict.get(n,0)+1
#     if dict[n]>1:
#         print("Array elements not unique") 
#         unique=False
#         break
# if  unique:
#     print("All elements are unique")

#set approach
uset=set(A)
if len(uset)!=len(A):
    print("Array elements not unique")
else:
    print("All elements are unique")
    