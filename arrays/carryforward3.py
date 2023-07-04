#carry fowrward/subarray
#Given an array , find the length of smallest subarray which contains both min and max of array

#observations
# the smallest subarray always has only one min and one max
# the min and max are always the last/edge elements in the subarray

#arr=[1,2,3,1,3,3,6,4,6,3]
arr=[834,563,606,221,165]
min_val=min(arr)
max_val=max(arr)

#brute force
#initialize answer to max length of array.. 
# keep going from left to right, 
# look for either min or max.. once found ..enter second loop to find min or max 
# i.e.if max found..loop for next min
# while doing so if you find again a max, break out of loop because new max is found and new iteration is needed
# if a min is found, calculate length of subaray and replace that with minimum of existing answer vs calculated length of subarray
#also, if min is found ..loop for next max
#while doing so if you find min again, break out of inner loop because new min is found and a new iteration is needed
#if a max is found, calculate length of subaray and replace that with minimum of existing answer vs calculated length of subarray

# if min_val==max_val:
#     ans=1
# ans=len(arr)   
# for i in range(0,len(arr)):
#     if arr[i]==min_val:
#         for j in range(i+1,len(arr)):
#             if arr[j]==min_val:
#                 break
#             if arr[j]==max_val:
#                 ans=min([ans,j-i+1])
#                 break
#     elif arr[i]==max_val:
#         for j in range(i+1,len(arr)):
#             if arr[j]==max_val:
#                 break
#             if arr[j]==min_val:
#                 ans=min([ans,j-i+1])
#                 break
# print(f"Answer is {ans}")

#optimized approach.. right to left with min_index and max index
ans=len(arr)
if min_val==max_val:
    ans=1
i=len(arr)-1
min_index=-1
max_index=-1
while i>=0:
    if arr[i]==min_val:
        min_index=i
        if max_index!=-1:
            ans=min([ans,max_index-min_index+1])
    if arr[i]==max_val:
        max_index=i
        if min_index!=-1:
            ans=min([ans,min_index-max_index+1])
    i-=1
print(f"Answer is {ans}")
   
