# given an array of N elements and Q queries, return True for each query if every element is strictly increasing
#A[ 2,3,4,5,6,7,1]
#Q1 [1,4] = True : [2,3,4,5]
#Q2 [ 5,7]= False : [ 6,7,1]


A=[ 2,3,4,5,6,7,8]
Q=[[1,4],[5,7]]
boolArray=[]
for i in range(len(A)-1):
    if A[i]<A[i+1]:
        boolArray.append(1)
    else:
        boolArray.append(0)
boolArray.append(1)
print(f"BoolArray {boolArray}")
     
psum=[]
psum.append(boolArray[0])

for i in range(1,len(boolArray)):    
    psum.append(psum[i-1]+boolArray[i])

print(psum)

for i in range(len(Q)):
    left=Q[i][0]-1
    right=Q[i][1]-1
    rangelength=right-left+1
    
    if left>0:
        rangesum=psum[right]-psum[left-1]    
    else: 
        rangesum=psum[right]
    print(f"left {left}")
    print(f"right {right}")
    print(f"rangelength : {rangelength}")
    print(f"rangesum : {rangesum}")
    print(rangesum==rangelength)
    
