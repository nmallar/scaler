#subarray with zero sum
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.
#approach
#compute prefix sum 
# if there is any repeating element in prefix sum, there is a subarray with sum zero
A=[1,-1]
print(f"Original array is {A}")

psum=[]
psum.append(A[0])
for i in range(1,len(A)):
    psum.append(psum[i-1]+A[i])

prefixset=set(psum)
print(f"prefix sum : {psum}")
if len(psum)!=len(prefixset) or 0 in prefixset:
    print(f" There exists a subarray with sum=0")
else:
    print(f" There is no subarray with sum=0")