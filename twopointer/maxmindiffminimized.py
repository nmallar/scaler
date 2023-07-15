# Advance : Two pointer
#Given3 sorted arrays A[],B[],C[] of size N, find i,j,k
# such that
# max(A[i],B[j],C[k])-min(A[i],B[j],C[k]) is minimized

#Approach : keep 3 pointers p1, p2 p3 in each array and start from begining and move the pointer with min value so that the difference in max and min is minimum
import sys
A=[3,14,16,20,29,40]
B=[-6,23,24,30,35,50]
C=[-15,15,26,31,39,42]

p1=0
p2=0
p3=0
answer=sys.maxsize
while p1<len(A) and p2<len(A) and p3<len(A):
    
    max1=max(A[p1],B[p2],C[p3])
    min1=min(A[p1],B[p2],C[p3])
    
    diff=max1-min1
    
    if diff<answer:
        answer=diff
    
    if min1==A[p1]:
        p1+=1
    elif min1==B[p2]:
        p2+=1
    else:
        p3+=1

print(f"min diff between max and min is diff is {answer}")
        