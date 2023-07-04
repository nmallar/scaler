
#pick from both sides
# You are given an integer array A of size N
# You have to perform B operation . In every operation you can remove either leftmost or rightmost element of array 
# Find and return the maximum possible sum of the B elements that were removed after B operations


#arr=[2,3,-1,4,2,1]
arr=[-533,-666,-500,169,724,478,358,-38,-536,705,-855,281,-173,961,-509,-5,942,-173,436,-609,-396,902,-847,-708,-618,421,-284,718,895,447,726,-229,538,869,912,667,-701,35,894,-297,811,322,-667,673,-336,141,711,-747,-132,547,644,-338,-243,-963,-141,-277,741,529,-222,-684,35]

B=48

print(f"Current array is { arr}")
print(f"Value of B is {B}")

currentSum=0
for i in range(0,B):
    currentSum+=arr[i]

max=currentSum


lptr=B-1
rptr=len(arr)-1

while(lptr>=0 and rptr>=0):
    currentSum+=arr[rptr]
    currentSum-=arr[lptr]
    lptr-=1
    rptr-=1
    if currentSum>max:
        max=currentSum


print(f"Max sum is  {max}")
    

