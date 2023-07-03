def getMax(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

def countMax(arr,max):
    maxCount=0
    for i in range(0,len(arr)):
        if arr[i]==max:
            maxCount+=1
    return maxCount

if __name__=="__main__":
    arr=[10,20,30,30,40,50,10,50]
    max=getMax(arr)
    maxCount=countMax(arr,max)
    print(f"The number of elements with atleast one element larger than itself are : {len(arr)-maxCount}")
    
