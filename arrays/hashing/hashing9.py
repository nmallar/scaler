#hashing
# Given an array of n elements
#calculate number of distinct elements in every subarray of size k

# A=[2,4,3,8,3,9,4,9,4,10]
# k=4
A=[1]
k=1

#hashset approack
# for i in range(0,len(A)-k+1):
#     hashset=set()
#     for j in range(i,i+k):
#         hashset.add(A[j])
#     print(len(hashset))
#     print( hashset)
    
    #TC: O(N*K) SC: (K)
    
#optimized version 
#sliding window with sliding window

dict={}
ans=[]
for i in range(0,k):
    if A[i] in dict:
       dict[A[i]]+=1
    else:
     dict[A[i]]=1
print(len(dict))
ans.append(len(dict))

for j in range(k,len(A)):
    dict[A[j-k]]-=1
   
    if dict[A[j-k]]==0:
        del dict[A[j-k]]
    if A[j] in dict:
        dict[A[j]]+=1
    else:
        dict[A[j]]=1    
    print(len(dict))   
    ans.append(len(dict))     
print(ans)
       
