A=['A','B','D','U','L','A','G','A','G']
count=0
answer=0
M = 1000000007
i=len(A)-1
while i>=0:
    if A[i]=='G':
        count+=1
    if A[i]=='A':
        answer=(answer+count)%M
    i=i-1
print(f"Answer is {answer}")
