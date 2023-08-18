#inversion count
#given an array , find number of pairs i, j such that
#i<j and A[i]>A[j]


class Solution:
    
    def mergesort(self,A,s,e):
        if s==e:
            return 0
        m=int((s+e)/2)
        leftpairs=self.mergesort(A,s,m)
        rightpairs=self.mergesort(A,m+1,e)
        betweenpairs=self.merge(A,s,m,e)
        return leftpairs+rightpairs+betweenpairs
    
    
    def merge(self,A,s,m,e):
        p1=s
        p2=m+1
        C=[]
        count=0
        while p1<=m and p2<=e:
            if A[p1]<A[p2]:
                C.append(A[p1])
                p1+=1
            else:
                C.append(A[p2])
                p2+=1
                count=count+(m-p1+1)
        
        while p1<=m:
            C.append(A[p1])
            p1+=1
        while p2<=e:
            C.append(A[p2])
            p2+=1
            
        for i in range(len(C)):
            A[s+i]=C[i]
        return count


sobject=Solution()
A=[2,8,4,-1,6,7,5,10]
A=[10,3,8,15,6,12,2,18,7,1]
print(f"Before sort {A}")
ans=sobject.mergesort(A,0,len(A)-1)
print(f"After  sort {A}")
print(f"Total pairs {ans}")