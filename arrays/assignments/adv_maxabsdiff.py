#Maximum Absolute Difference
#You are given an array of N integers, A1, A2, .... AN.
#Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.


#sub-optimal solution

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def maxArr(self, A):
#         max=0
#         for i in range(0,len(A)):
#             for j in range(i+1,len(A)):
#                 sum=0
#                 if i!=j:
#                     sum=abs(i-j)+abs(A[i]-A[j])
#                 if sum>max:
#                     max=sum
#         return max

#Solution approach
# An efficient solution in O(n) time complexity can be worked out using the properties of absolute values. 
# f(i, j) = |A[i] – A[j]| + |i – j| can be written in 4 ways (Since we are looking at max value, we don’t even care if the value becomes negative as long as we are also covering the max value in some way). 

# Case 1: A[i] > A[j] and i > j
# |A[i] - A[j]| = A[i] - A[j]
# |i -j| = i - j
# hence, f(i, j) = (A[i] + i) - (A[j] + j)

# Case 2: A[i] < A[j] and i < j
# |A[i] - A[j]| = -(A[i]) + A[j]
# |i -j| = -(i) + j
# hence, f(i, j) = -(A[i] + i) + (A[j] + j)

# Case 3: A[i] > A[j] and i < j
# |A[i] - A[j]| = A[i] - A[j]
# |i -j| = -(i) + j
# hence, f(i, j) = (A[i] - i) - (A[j] - j)

# Case 4: A[i] < A[j] and i > j
# |A[i] - A[j]| = -(A[i]) + A[j]
# |i -j| = i - j
# hence, f(i, j) = -(A[i] - i) + (A[j] - j)
# Note that cases 1 and 2 are equivalent and so are cases 3 and 4 and hence we can design our algorithm only for two cases as it will cover all the possible cases.

# 1. Calculate the value of A[i] + i and A[i] – i for every element of the array while traversing through the array.
# 2. Then for the two equivalent cases, we find the maximum possible value. For that, we have to store minimum and maximum values of expressions 
# A[i] + i and A[i] – i for all i.
# 3. Hence the required maximum absolute difference is maximum of two values i.e. max((A[i] + i) – (A[j] + j)) and max((A[i] – i) – (A[j] – j)).
# These values can be found easily in linear time. 
# a. For max((A[i] + i) – (A[j] + j)) Maintain two variables max1 and min1 which will store maximum and minimum values of A[i] + i respectively.
# max((A[i] + i) – (A[j] + j)) = max1 – min1 
# b. For max((A[i] – i) – (A[j] – j)). Maintain two variables max2 and min2 which will store maximum and minimum values of A[i] – i respectively.
# max((A[i] – i) – (A[j] – j)) = max2 – min2

import sys

A= [ -70, -64, -6, -56, 64,  61, -57, 16, 48, -98 ]
 

max1=-sys.maxsize
max2=-sys.maxsize
min1=sys.maxsize
min2=sys.maxsize

for i in range(len(A)):
    max1=max(max1,A[i]+i)
    min1=min(min1,A[i]+i)
    max2=max(max2,A[i]-i)
    min2=min(min2,A[i]-i)
    
print(max(max1-min1,max2-min2))