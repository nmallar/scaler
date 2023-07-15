#Advanced :two pointer
# Given N distinct sorted elements, check if there exists a pair(i,j),
#arr[i]+arr[j]=k, i != j


#array approach
# def pairExists(arr,k):    
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==k:
#                 return True                       
#     return False

# if __name__=="__main__":
#     arr=[10,20,30,30,40,50,10,50]
#     k=86 # answer False
#     k= 60 #True    
#     print(pairExists(arr,k))    
#  # TC - N(N-1)/2   
    
#using hashset
# A=[10,20,30,30,40,50,10,50]
# #k=86 # answer False
# k= 60 #True    
# dict=set()
# pairFound=False
# for i in range(len(A)):
#    a=A[i]
#    b=k-a
#    if b in dict:
#        print("Pair found")
#        pairFound=True
#        break
#    else:
#        dict.add(a)
# if not pairFound:
#     print("Pair does not exist")

#using two pointer
A=[10,20,30,30,40,50,10,50]
#k=86 # answer False
k= 60 #True 
p1=0
p2=len(A)-1
pairfound=False
while p1<p2:
    if A[p1]+A[p2]==k:
        pairfound=True
        break
    elif  A[p1]+A[p2]>k:
        p2-=1
    else:
        p1+=1
          
if pairfound:
     print("Pair found")
else:
    
    print("Pair not found")
     