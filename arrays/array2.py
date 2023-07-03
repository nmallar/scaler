#2. Given an array of N elements return true if the array contains two elements A[i] and A[j] such that
# A[i]+A[j]=k and i!=j otherwise return false


def pairExists(arr,k):
    
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                return True                       
    return False

if __name__=="__main__":
    arr=[10,20,30,30,40,50,10,50]
    k=86
    
    print(pairExists(arr,k))
    
 # TC - N(N-1)/2   
    