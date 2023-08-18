# Problem Description
# You are given a sorted array A of size N and a target value B.
# Your task is to find the index (0-based indexing) of the target value in the array.

# If the target value is present, return its index.
# If the target value is not found, return the index of least element greater than equal to B.
# Your solution should have a time complexity of O(log(N)).


# Problem Constraints
# 1 <= N <= 106
# 1 <= A[i] <= 105
# 1 <= B <= 105



# Input Format
# The first argument is an integer array A of size N.
# The second argument is an integer B.



# Output Format
# Return an integer denoting the index of target value.



# Example Input
# Input 1:

# A = [1, 3, 5, 6]
# B = 5 
# Input 2:

# A = [1, 4, 9]
# B = 3


# Example Output
# Output 1:

# 2 
# Output 2:

# 1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        low=0
        high=len(A)-1
        ans=0
        while low <=high:
            mid=(low+high)//2
            if A[mid]==B:
                return mid
            elif A[mid]>B: #go left
                high=mid-1
            else:           # go right
                low=mid+1
                ans=low
        return ans
s=Solution()
A =[ 17, 30, 32, 69, 94, 96, 106, 118, 127, 159, 169, 170, 178, 183, 209, 238, 242, 247, 253, 261, 265, 279, 288, 302, 305, 316, 352, 357, 374, 376, 392, 402, 410, 421, 439, 442, 444, 446, 454, 458, 464, 467, 468, 498, 500, 513, 523, 541, 545, 556, 575, 608, 616, 629, 631, 635, 669, 674, 682, 686, 693, 695, 719, 733, 754, 755, 756, 778, 802, 822, 824, 828, 835, 847, 848, 862, 864, 878, 883, 885, 904, 908, 928, 934 ]
B = 104
print(s.searchInsert(A,B))