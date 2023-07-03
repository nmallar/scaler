#3. Given an array ..reverse it with space complexity of O(1)

def reverseArray(arr):
    
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        
        i+=1
        j-=1
    return arr   

if __name__=="__main__":
    arr=[10,20,30,80,40,50]
    print(f"Original Array {arr}")
    print(f"Reversed Array {reverseArray(arr)}")