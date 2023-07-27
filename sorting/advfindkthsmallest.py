#advanced sorting1
# given array of N elements find Kth smallest element
#approch selection sort
#A=[2,8,4,-1,6,7,5,10]
A=[8,16,80,55,32,8,38,40,65,18,15,45,50,38,54,52,23,74,81,42,28,16,66,35,91,36,44,9,85,58,59,49,75,20,87,60,17,11,39,62,20,17,46,26,81,92]
B=9
print(f"Before sorting : {A}")

for i in range(len(A)-1):
    if i==B:
        break
    
    min=A[i]
    index=i
    for j in range(i,len(A)):
        if A[j]<min:
            min=A[j]
            index=j
    A[i],A[index]=A[index],A[i]
print(A[B-1])
    
# print(f"After sorting : {A}")
# print(f"{k} th smallest element is {A[k-1]}")

