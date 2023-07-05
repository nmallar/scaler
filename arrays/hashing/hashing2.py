#hashing
#1. Find the first non repreating element

A=[2,10,3,9,2,9,2,3,8,10,8,7]
print(f"Original array is {A}")
dict={}
for n in A:
    dict[n]=1+dict.get(n,0)

found=False
for i in range(0,len(A)):
    if dict[A[i]]==1:
        print(f" {A[i]} is the first non repeating element")
        found=True
        
        break
if not found:
    print(f"No non repeating element exists")
