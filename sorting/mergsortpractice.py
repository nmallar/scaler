class Solution:
    
    def mergesort(self, A,s,e):
        if s==e:
            return
        
        middle=(s+e)//2
        self.mergesort(A,s,middle)
        self.mergesort(A,middle+1,e)
        self.merge(A,s,middle,e)
    
    def merge(self,A,start,middle,end):
        
        p1=start
        p2=middle+1
        temp=[]
        while p1<=middle and p2<=end:
            if A[p1]<A[p2]:
                temp.append(A[p1])
                p1+=1
            else:
                temp.append(A[p2])
                p2+=1
        while p1<=middle:
            temp.append(A[p1])
            p1+=1
        while p2<=end:
            temp.append(A[p2])
            p2+=1
        for i in range(len(temp)):
            A[start+i]=temp[i]
            
sobject=Solution()
A=[2,8,4,-1,6,7,5,10]
print(f"Before sort {A}")
sobject.mergesort(A,0,len(A)-1)
print(f"After  sort {A}")