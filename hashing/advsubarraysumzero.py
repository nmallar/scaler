#advance Hashing
#Given an array check if subarray with sum=0 exists

#brute force : checkk all elements O(N3)= O(n2)*n where o(n2 ) for all subarray sums
# burte force with carry forward its O(n2)
#prefix sum array - if there is a duplicate sum in prefix array - it means there is a subarray with sum=0
# this is an extra function
def psumandhash():
    psum=[]
    dict={}
    psum.append(A[0])
    dict[A[0]]=1
    for i in range(1,len(A)):
        psum.append(psum[i-1]+A[i])
        if psum[i] in dict:
            dict[psum[i]]+=1
        else:
            dict[psum[i]]=1
    print(A)
    print(psum)
    print(dict)  

A=[2,2,1,-3,4,3,1,-2,-3,2]

psum=[]
hashset=set()
found=False
if 0 in A:
    found=True
else:   
    psum.append(A[0])
    hashset.add(A[0])

    for i in range(1,len(A)):
        psum.append(psum[i-1]+A[i])
        if psum[i] in hashset :
            found=True
            break
        else:
            hashset.add(psum[i])
        
    if 0 in psum:
        found==True
print(found)



