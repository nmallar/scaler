#merge sort


class Solution:
    
    def mergesort(self,A,s,e):
        if s==e:
            return
        m=int((s+e)/2)
        self.mergesort(A,s,m)
        self.mergesort(A,m+1,e)
        self.merge(A,s,m,e)
    
    
    def merge(self,A,s,m,e):
        p1=s
        p2=m+1
        C=[]
        
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
            A[s+i]=C[i]


sobject=Solution()
A=[2,8,4,-1,6,7,5,10]
print(f"Before sort {A}")
sobject.mergesort(A,0,len(A)-1)
print(f"After  sort {A}")