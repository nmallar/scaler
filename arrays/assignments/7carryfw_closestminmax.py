
    # @param A : list of integers
    # @return an integer
A=[834,563,606,221,165]
    
min_val=min(A)
max_val=max(A)
if min_val==max_val:
    print(f"Answer is 1") 
min_index=-1
max_index=-1
i=len(A)-1
ans=len(A)
while i>=0:
    if A[i]==min_val:
        min_index=i
        if max_index!=-1:
            ans=min([ans,max_index-min_index+1])
    if A[i]==max_val:
        max_index=i
        if min_index!=-1:
            ans=min([ans,min_index-max_index+1])
    i-=1
print(f"Answer is {ans}")
