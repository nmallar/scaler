#adv hashing assignment
#Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
#If the given array contains a sub-array with sum zero return 1, else return 0.
# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        psum=[]
        psum.append(A[0])
        if 0 in A:
            return 1
        for i in range(1,len(A)):
            psum.append(psum[i-1]+A[i])
        hashset=set(psum)
        
        if len(hashset) != len(psum) or 0 in psum:
            return 1
        return 0
        


s=Solution()
#A = [1, 2, 3, 4, 5]
A=[1, 2, 3, 4, 5,0]
#A = [4, -1, 1]
print(s.solve(A))

