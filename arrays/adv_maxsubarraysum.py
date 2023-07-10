# Given an array of N elements
# find max subarray sum

#approach ..use carry forward method
#keep adding to sum as long as sum >0
# keep udating answe if sum is greater than answer (answer starts with minium integer value (INT_MIN))
# if sum<0 , update sum to zero before moving forward.
#kadane's algo

import sys

#A=[10,20,30,-40,50,-60]
A=[5,6,7,-3,2,-10,-12,8,12,21,-4,7]
answer=-sys.maxsize
sum=0

for i in range(0,len(A)):
    sum+=A[i]
    if sum>answer:
        answer=sum
    if sum<=0:
        sum=0
print(answer)