#4 Given an array of N elements
# and [start,end],
#reverse the array from start to end
# Note: start<=end
def reverseArray(arr,start,end):
    i=start
    j=end
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]        
        i+=1
        j-=1
    return arr   

if __name__=="__main__":
    arr=[10,40,30,90,45,23,55]
    start=3
    end=6
    print(f"Original Array {arr}")
    print(f"Reversed Array {reverseArray(arr,start ,end)}")
