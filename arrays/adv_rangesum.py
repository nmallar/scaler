#Given N array elements, and Q queries find the the sum of elements in each range
#sum[left,right]=prefixsum[right]-prefix[left-1]

A=[1,2,3,4,5,6,7,8,9]
Q=[[1,2],[3,5]]
print(A)
print(Q)

# prefix sum approach TC: O(N+Q*1) SC : O(N) used for prefixsum
# psum=[]
# psum.append(A[0])
# for i in range(1, len(A)):
#     psum.append(psum[i-1]+A[i])
# for i in range(len(Q)):
#     left=Q[i][0]-1
#     right=Q[i][1]-1
#     if left>0:
#         rangesum=psum[right]-psum[left-1]    
#     else: 
#         rangesum=psum[right]
#     print(rangesum)



# if we are allowed to modify the array then SC: O(1) and we use same array to store prefix sum

# psum=[]
# psum.append(A[0])
for i in range(1, len(A)):
    A[i]=A[i-1]+A[i]
for i in range(len(Q)):
    left=Q[i][0]-1
    right=Q[i][1]-1
    if left>0:
        rangesum=A[right]-A[left-1]    
    else: 
        rangesum=A[right]
    print(rangesum)