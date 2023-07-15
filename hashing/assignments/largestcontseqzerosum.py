#hashing
# Given an array A of N integers.

# Find the largest continuous sequence in a array which sums to zero.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
                       
        psum=[]
        psum.append(A[0])
        dict={}
        dict[0]=-1
        dict[A[0]]=0
        ls=[]

        for i in range(1,len(A)):
            psum.append(psum[i-1]+A[i])
            if psum[i] not in dict:
                dict[psum[i]]=i

        print(A)
        print(psum)
        print(dict)    
        answer=0
        for i in range(len(psum)):    
            if psum[i] in dict:        
                length=i-dict[psum[i]]
                
                if length>answer:
                    ls=A[dict[psum[i]]+1:i+1]
                    answer=length
        if answer==0 and len(ls)==0 and 0 in psum:
            ls=[0]
        return ls
            

A=[1,-1,2,-2]
#A=[1,2,-2,4,-4]
#A=[1,2,-3,3]
A=[0,22,7,21,-11,-6,-7,-16,-2]
#A=[3,4,9,7]
#A=[2,2,1,-3,4,3,1,-2 ,-3,2]
#A=[-1,4,-3,2]
s=Solution()
print(s.lszero(A))