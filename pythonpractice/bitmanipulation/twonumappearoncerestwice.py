# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.

# Note: Return the two numbers in ascending order.


# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109



# Input Format
# The first argument is an array of integers of size N.



# Output Format
# Return an array of two integers that appear only once.



# Example Input
# Input 1:
# A = [1, 2, 3, 1, 2, 4]
# Input 2:

# A = [1, 2]


# Example Output
# Output 1:
# [3, 4]
# Output 2:

# [1, 2]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        pass
        
        val=0
        for num in A:
            val=val^num
        
        for i in range(30):            
            if (val>>i) & 1 ==1:
                pos=i
                break
        set=0
        unset=0
        for num in A:
            if (num>>pos) & 1==1:
                set=set^num
            else:
                unset=unset^num
        if set>unset:
            return [unset,set]
        return [set,unset]
A = [1, 2, 3, 1, 2, 4]
s=Solution()
print(s.solve(A))