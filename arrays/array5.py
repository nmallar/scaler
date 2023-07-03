#5.Given an array of N elements
# rotate the array from last to first by k times 
#SC : O(1)

def reverseArray(arr,start,end):
    
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

def rotateArray(arr,k):
    k=k%len(arr)
    if k==0:
        return arr
    reverseArray(arr,0,len(arr)-1)
    reverseArray(arr,0,k-1)
    reverseArray(arr,k,len(arr)-1)
    return arr
    

arr=[10,40,30,90,45,23,55]
k=7
print(f"Original Array {arr}")
print(f"Reversed Array {rotateArray(arr,k)}")