# given 2 sorted arrays A[N], B[M], merge and create and return a sorted array.

A=[-5,1,3,7,10,12,15]
B=[-4,0,2,8,9]
print(f"A : {A}")
print(f"B : {B}")
C=[]
p1=0
p2=0
#p3=0
while p1<len(A) and p2<len(B):
    if A[p1]<B[p2]:
        C.append(A[p1])
        p1+=1
      #  p3+=1
    else:
        C.append(B[p2])
        p2+=1
      #  p3+=1
        
while p1<len(A):
    C.append(A[p1])
   # p3+=1
    p1+=1

while p2<len(B):
    C.append(B[p2])
   # p3+=1
    p2+=1

print(f"C : {C}")
