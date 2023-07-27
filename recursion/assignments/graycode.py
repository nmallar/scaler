# #adv reecursion
# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

# A gray code sequence must begin with 0.

# Input Format
# The first argument is an integer A.



# Output Format
# Return an array of integers representing the gray code sequence.

# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].

# for A = 1 the gray code sequence is:
#     00 - 0
#     01 - 1
# So, return [0, 1].

class Solution:
    # @param A : integer
    # @return a list of integers
    #non recursive
    def grayCode(self, A):        
        ans=[0]        
        for i in range(A):            
            for j in reversed(range(len(ans))):
                ans.append(ans[j] | 1<<i)
        return ans

    
    def grayCodeRecursive(self,A):
        if A==0:
            return ['']
        first_half=self.grayCodeRecursive(A-1)
        second_half=first_half.copy()
        first_half=['0'+ code for code in first_half]
        second_half=['1'+ code for code in reversed(second_half)]
        return first_half+second_half
s=Solution()
print(s.grayCodeRecursive2(4))



