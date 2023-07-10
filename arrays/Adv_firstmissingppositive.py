#Arrays advanced
#Given N array elements, find first missing +ve integer

# arr[5]= 3 -2 1 4 5 : ans:2
#answer always is between 1 to N+1 .. all other numbers including zero and negative numbers are to be ignored

#approach 1

#iterate through the array O(n2)

#A= [3, -2,0, 1, 4, 5]

# for i in range(1,len(A)+1):
#     present=False    
#     for num in A:
#         if num==i:
#             present=True
#             break
#     if not present:
#         print(i)
#         break           

# if present :
#     print(len(A)+1)
        
#iterate through the array using hashset

# hashhset=set()
# for num in A:
#     hashhset.add(num)

# missingElementFound=False
# for i in range(1, len(A)+1):
#     if i not in hashhset:
#         print(i)
#         missingElementFound=True
#         break
# if not missingElementFound:
#     print(len(A)+1)
     
#implement without any built in library


#approach of creating bool list of size 1 to N

# boolList=[]

# for i in range(0,len(A)):
#     boolList.append(False)

# for i in range(0,len(A)):
#     if A[i]>=1 and A[i]<=len(A):
#         boolList[A[i]-1]=True
        
# missingElementFound=False

# for i in range(0,len(A)):
#     if boolList[i]==False:
#         print(i+1)
#         missingElementFound=True
#         break
    
# if missingElementFound==False:
#     print(len(A)+1)



#implement without any built in library no extra space
#approach exisitng array itself

#update negative number with large value(N+2)
# for each number found , go to its position and mark its current value as negative
# [3,5,6] for 3 mark 6 (at position 3-1 = 2) with negative to mark 3 is present
A= [3, 2,0, 1, 4, 6]


#modify irrevalant array elements (zero and negatives) with a value that can never be the right answer(N+2) . Valid answer is always between 1 to N

for i in range(0,len(A)):
    if A[i]<=0:
        A[i]=len(A)+2

# modify the relevant array elements with negative sign to indicate that the array element exists in array.
for i in range(0,len(A)):
    element=abs(A[i])
    if element>=1 and element<=len(A)+1:
        A[element-1]=-1*abs(A[element-1])

#search for first  element with positive value dentoing its index position element is missing
missingElementFound=False
for i in range(0,len(A)):
    if A[i]>0:
        print(i+1)
        missingElementFound=True
        break
if not missingElementFound:
    print(len(A)+1)
    
    
    
    
        