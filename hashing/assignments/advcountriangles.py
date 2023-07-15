#Problem Description
#Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.
#
#Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.
#NOTE: The answer may be large so return the answer modulo (109 + 7).


class Solution:
    
    def solve(self,A,B):
        xhash={}
        yhash={}
        M = 1000000007
        for i  in range(len(A)):
            if A[i] in xhash:
                xhash[A[i]]+=1
            else:
                xhash[A[i]]=1
            if B[i] in yhash:
                yhash[B[i]]+=1
            else:
                yhash[B[i]]=1
        countx=0
        county=0
        answer=0
        # for i in range(len(A)):
        #     if A[i]==xhash[A[i]]:
        #         xcount+=1
        #     if B[i]==yhash[B[i]]:
        #         ycount+=1
                
        #     answer=answer+(xcount-1)*(ycount-1)
        print(xhash)
        print(yhash)
        for i in range(len(A)):
            # if A[i]==xhash[A[i]]:
            #     xcount+=1
            # if B[i]==yhash[B[i]]:
            #     ycount+=1
                
            answer=answer+((xhash[A[i]]-1)*(yhash[B[i]]-1))%M
                
        
        print(answer)
        

# A=[5,5,5,5,5,2,7,9]
# B=[9,8,6,4,2,6,6,6,6]
# A=[1,3,5,1,1]
# B=[3,3,3,1,5]
A=[1,2,2,2,3]
B=[2,1,2,3,2]
s=Solution()
s.solve(A,B)
