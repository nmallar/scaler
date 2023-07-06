#hashing
# Given an array A of N integers.

# Find the largest continuous sequence in a array which sums to zero.
#A=[3,4,9,7]
#A=[2,2,1,-3,4,3,1,-2 ,-3,2]
#A=[-1,4,-3,2]
A=[1,2,-2,4,-4]
print(f"Original array is {A}")
max_len=0
current_sum=0
dict={}

for i in range(len(A)):
    current_sum+=A[i]
    if current_sum==0:
        max_len=i+1
    if current_sum in dict:
        max_len=max(max_len, i-dict.get(current_sum))
    else:
        dict[current_sum]=i
print(max_len)      

# prefixset=set(psum)
# if len(psum)!=len(prefixset) or 0 in prefixset:
#     print(f" There exists a subarray with sum=0")
# else:
#     print(f" There is no subarray with sum=0")