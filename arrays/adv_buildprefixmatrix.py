# try to build the prefix sum matrix for given N*M matrix
# and then answer range query questions




N=4
M=5
A= [ [1,  2,  3,  4,  5],\
     [6,  7,  8,  9,  10],\
     [11, 12, 13, 14, 15],\
     [16, 17, 18, 19, 20]]
psmatrix=[]

for i in range(0,N):
    psmatrix.append([0])
    
#rowsum
for i in range(0,N):
    psmatrix[i][0]=A[i][0]
    for j in range(1,M):
        psmatrix[i].append(psmatrix[i][j-1]+A[i][j])
        
        
#colsum      
for i in range(0,M):
    #psmatrix[0][i]=psmatrix[0][i]  
    for j in range(1,N):
        psmatrix[j][i]=psmatrix[j-1][i]+psmatrix[j][i]
        
        
for i in range(0,N):
    print(psmatrix[i])
    
Q=[[1,3],[4,5]]

a1=Q[0][0]-1
b1=Q[0][1]-1
a2=Q[1][0]-1
b2=Q[1][1]-1
print(f"{a1} :{b1} {a2}: {b2}")
sum=psmatrix[a2][b2]
if b1>0:
    sum=sum-psmatrix[a2][b1-1]
if a1>0:
    sum=sum-psmatrix[a1-1][b2]
if a1>0 and b1>0:
    sum = sum + psmatrix[a1-1][b1-1]
    
print(f"Sub matrix sum is {sum}")