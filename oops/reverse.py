class Solution:
    
    def solve(self,A,B):
        
        for i in range(len(A)):
            if A[i]==B:
                return [A[i], A[i]]
            elif i>0 and A[i-1] <=B <= A[i+1]:
                return [A[i-1],A[i+1]]