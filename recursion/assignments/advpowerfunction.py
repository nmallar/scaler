#adv recursion

#Implement pow(A, B) % C.
#In other words, given A, B and C, Find (AB % C).$
#Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        if A==0:
            return 0
        if B==0:
            return 1
        
        powerfun=self.pow(A,int(B/2),C)
        if B%2==0:
            return (powerfun * powerfun)%C
        else:
            return ( (powerfun * powerfun)%C * A%C)%C
        

s=Solution()
print(s.pow(0,0,1))


        
