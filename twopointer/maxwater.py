# given an array of N elements with each element denoting the height of the wall, find out i and j such that water contained between the walls i and j is maximum
#A[i] denotes height of ith wall and A[j] denotes height of jth wall
#total water that can be stored = A[j]-A[i] * the width of the wall (j-i)
# approach two pointers.. start and end .. 
# in each iteration pick up the wall with least height and multiply it with available width.. that is the answer for that iteration.
# in every iteration, move the pointer of the wall will least height


#A=[4,5,1,2,3] # answer=12
A=[3,5,4,7,3,6,5,4,1,2]

p1=0
p2=len(A)-1
answer=0

while p1<p2:
    heightOfWall=min(A[p1],A[p2])
    width=p2-p1
    totalStorage=heightOfWall*width
    if totalStorage>answer:
        answer=totalStorage
    if A[p1]<A[p2]:
        p1+=1
    else:
        p2-=1
print(answer)