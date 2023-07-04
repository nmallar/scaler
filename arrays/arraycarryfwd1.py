#carry forward
# 1. given an array of characters , count number of ouccerences of pair <a,g> where s[i] = a and s[j]=g and i<j

arr=['a','c','g','d','g','a','g']
print(f"Original Array is  : {arr}")

#brute force approach
# pairCount=0

# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i]=='a' and arr[j]=='g':
#             pairCount+=1
# print(f"Pair count is : {pairCount}")


#optimized

# pairCount=0

# for i in range(0,len(arr)-1):
#     if arr[i]=='a':
#         for j in range(i+1,len(arr)):
#             if arr[j]=='g':
#                 pairCount+=1
# print(f"Pair count is : {pairCount}")

#start from right to left

i=len(arr)-1
gcount=0
answer=0
while i>=0:
    if arr[i]=='g':
        gcount+=1
    if arr[i]=='a':
        answer+=gcount
    i-=1
print(f"Pair count is : {answer}")
