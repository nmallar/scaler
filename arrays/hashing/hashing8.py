#2. Given an array of N elements return count of pairs i j  such that
# A[i]-A[j]=k and i!=j
#PENDING....
A=[10,20,30,30,40,50,10,50]
k=20

#using hashset

dict=set()
count=0
pairFound=False
for i in range(len(A)):
   a=A[i]
   b=k+a
   if b<0:
    b=b*-1
   print(f"  {a} - {b}= {k}")
   if  b in dict :
       count+=1
       pairFound=True
       
   else:
       dict.add(a)
if not pairFound:
    print("Pair does not exist")
else:
    print(f"Found {count} pairs")
   
   
   
   
