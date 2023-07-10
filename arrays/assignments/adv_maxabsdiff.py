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
#f(i, j) = |A[i] - A[j]| + |i - j| can be written in 4 ways 
# (Since we are looking at max value, we don’t even care if the value becomes negative as long as we are also covering the max value in some way).

# (A[i] + i) - (A[j] + j)
# -(A[i] - i) + (A[j] - j) 
# (A[i] - i) - (A[j] - j) 
# (-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)
# note that case 1 and 4 are equivalent and so are case 2 and 3.

# We can construct two arrays with values: A[i] + i and A[i] - i. Then, for the above 2 cases, we find the maximum value possible. 
# For that, we just have to store minimum and maximum values of expressions A[i] + i and A[i] - i for all i.

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