#advanced sorting1
# given array of N element
# sort only adjacent elements - bubble sort
#bubble sort : items not swapped if the are same..hence its stable sort


A=[2,8,4,-1,6,7,5,10]

print(f"Before sorting : {A}")

for i in range(len(A)-1):
    swapcount=0
    for j in range(len(A)-i-1): # optmized..because end of each iteration, last element is sort so no need to go till end
       if A[j]>A[j+1]:
           A[j],A[j+1]=A[j+1],A[j]
           swapcount+=1
    if swapcount==0: # indicates all items are already sorted and can stop further iterations      
        break
    
    
    
print(f"After sorting : {A}")
