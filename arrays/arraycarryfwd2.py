#carry forward
#Given an array, you have to find all leaders in the array.
#An element is a leader, if it is strictly greater than all elements on its right side.
# note arr[N-1] is always a leader as it has nothing to its right


arr=[18,14,6,2,8,4,7]

leader=arr[len(arr)-1]
leaderCount=1
i=len(arr)-2
while i==0 or i>0:
    if arr[i]>leader:
        leader=arr[i]
        leaderCount+=1              
    i-=1

print(f"Number of leaders are {leaderCount}")
print(max(1,2))