#adv recursion
#Given a number A, check if it is a magic number or not.
#A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively
# by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self,A):
        total=self.sum(A)
        while total>9:
            total=self.sum(total)        
        return 1 if total==1 else 0
    
    def sum(self, A):             
        if A==0: 
            return 0
        return self.sum(int(A/10))+A%10
       
        
s=Solution()
A=1291
print(s.solve(A))