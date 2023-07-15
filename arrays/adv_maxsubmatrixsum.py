#Given a matrix of size N*M, find max submatrix sum

#approach 
#build a prefix sum of the matrix with columnwise sum 
# for each iteration , you will get an array of prefix sums.
#use kadane's algorithm to find the maxium subarray from the given array..
# keep replacing maximum based on output got from kadane's algorithm and the existing max sum.
#PENDING with column prefix sum

import sys
def KadaneMaxSum(A):
    answer=-sys.maxsize
    sum=0

    for i in range(0,len(A)):
        sum+=A[i]
        if sum>answer:
            answer=sum
        if sum<=0:
            sum=0
    return answer

N=4
M=5
A= [ [1,  2,  3,  4,  5],\
     [6,  7,  8,  9,  10],\
     [11, 12, 13, 14, 15],\
     [16, 17, 18, 19, 20]]
psmatrix=[]

for i in range(0,M):
    psmatrix.append(A[0][i])
   

print(psmatrix)    
#colsum      
for i in range(0,M):
    #psmatrix[i].append(A[0][i])  
    for j in range(1,N):
        psmatrix.append(psmatrix[j-1][i]+psmatrix[j][i])
        
        
for i in range(0,N):
    print(psmatrix[i])

finalanswer=-sys.maxsize   
for rowstart in range(0,N):
    maxsumsubarray=[]
    for rowend in range(rowstart,N):
        maxsumsubarray.append(psmatrix[rowstart][rowend])
        finalanswer=max(finalanswer,KadaneMaxSum(maxsumsubarray))

print(f"Max submatrix sum is {finalanswer}")