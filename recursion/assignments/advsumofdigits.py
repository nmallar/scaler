#advance-recursion
#Given a number A, we need to find the sum of its digits using recursion.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==0:
            return 0
        return self.solve(int(A/10))+A%10
s=Solution()
A=345
print(s.solve(A))