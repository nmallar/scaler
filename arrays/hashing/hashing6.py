#2. Given an array of N elements return true if the array contains two elements A[i] and A[j] such that
# A[i]+A[j]=k and i!=j otherwise return false

A=[10,20,30,30,40,50,10,50]
k=100
#array approch 

# def pairExists(arr,k):
    
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==k:
#                 return True                       
#     return False

# if __name__=="__main__":
#     arr=[10,20,30,30,40,50,10,50]
#     k=86
    
#     print(pairExists(arr,k))
    
    
#using hashmap

# dict={}
# for i in range(len(A)):
#     if A[i] in dict:
#        dict[A[i]]=1+dict.get(A[i])
#     else:
#         dict[A[i]]=1
# pairFound=False
# for (key,value) in dict.items():
#     b=k-key
#     if key==b and value>1:
#         print("Pair exists")
#         pairFound=True
#         break
#     elif key !=b and b in dict:
#         print("Pair exists")
#         pairFound=True
#         break
# if not pairFound:
#     print("Pair does not exist")


#using hashset

dict=set()
pairFound=False
for i in range(len(A)):
   a=A[i]
   b=k-a
   if b in dict:
       print("Pair found")
       pairFound=True
       break
   else:
       dict.add(a)
if not pairFound:
    print("Pair does not exist")
   
   
   
   
