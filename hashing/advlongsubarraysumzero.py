#advance Hashing
#Given an array find length of longest subarray with sum =0

#approach with hashmap and edge case (entire array sum=0 using psum[i]==0 check in loop)
#A=[3,3,4,-5,-2,2,1,-3,3,-1,5,-4,-1]
# A=[1,-1,2,-2]
# psum=[]
# psum.append(A[0])
# dict={}
# dict[A[0]]=0

# for i in range(1,len(A)):
#     psum.append(psum[i-1]+A[i])
#     if psum[i] not in dict:
#         dict[psum[i]]=i


# print(A)
# print(psum)
# print(dict)    
# answer=0
# for i in range(len(psum)):
#     #edge case A=[1,-1,2,-2] here psum has only one sum=0 but entire array sum is zero. 
#     # So, to handle that we check for max length when psum becomes zero and current answer. In case of entire array sum zero, i+1=length of array
#     if psum[i]==0:
#         answer=max(answer,i+1)
#         continue
#     if psum[i] in dict:        
#         length=i-dict[psum[i]]
#         if length>answer:
#             answer=length
        
# print(f"Longest subarray with sum=0 has length of {answer}")


#approach 2 with hashmap and edge case handled automaticall by putting <0,-1> hashmap entry indicating sum of zero in -1th index position


#A=[3,3,4,-5,-2,2,1,-3,3,-1,5,-4,-1]
A=[1,-1,2,-2] # to test edge case of entire array sum zero
psum=[]
psum.append(A[0])
dict={}
dict[0]=-1
dict[A[0]]=0

for i in range(1,len(A)):
    psum.append(psum[i-1]+A[i])
    if psum[i] not in dict:
        dict[psum[i]]=i

print(A)
print(psum)
print(dict)    
answer=0
for i in range(len(psum)):    
    if psum[i] in dict:        
        length=i-dict[psum[i]]
        if length>answer:
            answer=length
        
print(f"Longest subarray with sum=0 has length of {answer}")