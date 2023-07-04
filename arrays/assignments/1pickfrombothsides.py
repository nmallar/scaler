
#pick from both sides
# You are given an integer array A of size N
# You have to perform B operation . In every operation you can remove either leftmost or rightmost element of array 
# Find and return the maximum possible sum of the B elements that were removed after B operations


arr=[2,3,-1,4,2,1]
B=3

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
    

