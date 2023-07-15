#hashing
#given an array of N elements check 
#if there exists a subarray with sum=0
#approach
#compute prefix sum 
# if there is any repeating element in prefix sum, there is a subarray with sum zero
#A=[3,4,9,7]
#A=[2,2,1,-3,4,3,1,-2 ,-3,2]
#A=[-1,4,-3,2
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