#Advanced :two pointer
# Given N distinct sorted elements, check if there exists a pair(i,j),
#arr[i]-arr[j]=k,  and k>0 and i != j

#using two pointer
A=[10,20,30,30,40,50,10,50]
#k=86 # answer False
k= 30 #True
k=abs(k) 
p1=0
p2=1
pairfound=False
while p2<len(A)-1:
    if A[p2]-A[p1]==k:
        pairfound=True
        break
    elif  A[p2]-A[p1]>k:
        p1+=1
        if p1==p2:
            p2+=1
    else:
        p2+=1
          
if pairfound:
     print("Pair found")
else:
    
    print("Pair not found")
     