
# all elements appear thrice except one unique element that occurs twice.

A=[17,12,12,13,13,14,16,14,12,13,14,15,15,15,16,17,17]

ans=0
for i in range(32):
    count=0
    for j in range(len(A)):
        if (A[j]>>i) & 1 ==1 :
            count+=1
    if count%3==2:
        ans=ans | (1<<i) 

print(ans)