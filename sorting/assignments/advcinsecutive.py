
A=[8,16,80,55,32,8,38,40,65,18,15,45]

for i in range(len(A)-1):    
    min=A[i]
    index=i
    for j in range(i,len(A)):
        if A[j]<min:
            min=A[j]
            index=j
    A[i],A[index]=A[index],A[i]