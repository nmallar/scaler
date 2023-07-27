#Given N array elements and 3 indices s,m,e 
#where the subrray from s-m is sorted and m to e is also sorted.
# merge the two subarrays to created one sorted array from s to e keeping all other elements unchanged.

class Solution:


    def mergesorted(self, A, B, C):
        p1=0
        p2=0
        #p3=0
        while p1<len(A) and p2<len(B):
            if A[p1]<B[p2]:
                C.append(A[p1])
                p1+=1      
            else:
                C.append(B[p2])
                p2+=1   
                
        while p1<len(A):
            C.append(A[p1])   
            p1+=1

        while p2<len(B):
            C.append(B[p2]) 
            p2+=1
            
            
    def mergesortsubarray(self, A, s,m,e,C):
        p1=s
        p2=m+1
        
        #p3=0
        while p1<=m and p2<=e:
            if A[p1]<A[p2]:
                C.append(A[p1])
                p1+=1      
            else:
                C.append(A[p2])
                p2+=1   
            
        while p1<=m:
            C.append(A[p1])   
            p1+=1

        while p2<=e:
            C.append(A[p2]) 
            p2+=1
        
       
        for i in range(len(C)):
            A[i+s]=C[i]
            
     
        print(f"A : {A}")
            



#A=[-5,1,3,7,10,12,15,4,-3,6,8]
A=[4,8,-1,2,6,3,4,7,13,0]
#B=[-4,0,2,8,9]
C=[]
print(f"A : {A}")
#print(f"B : {B}")
sobj=Solution()
#sobj.mergesorted(A,B,C)
#print(f"C : {C}")

s=2
m=4
e=7
sobj.mergesortsubarray(A,s,m,e,C)
