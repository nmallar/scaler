
# Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i].

# He wants to select some trees to replace his broken branches.

# But he wants uniformity in his selection of trees.

# So he picks only those trees whose heights have frequency B.

# He then sums up the heights that occur B times. (He adds the height only once to the sum and not B times).

# But the sum he ended up getting was huge so he prints it modulo 10^9+7.

# In case no such cluster exists, Groot becomes sad and prints -1.
# scaler program method
# def getSum( A, B, C):

#         dict={}
#         for num in C:
#             if num in dict:
#                 dict[num]=1+dict.get(num)
#             else:
#                 dict[num]=1
#         sum=0
#         for (key,value) in dict.items():
#             if value==B:
#                 sum+=value
#         return sum

# print(f"Getsum {getSum(5,2,[1,2,2,3,3])}")

    
A = [1, 2, 2,2,3,3,4,4, 3]
C=len(A)
B=2

dict={}


for i in range(len(A)):
    if A[i] in dict:
       dict[A[i]]=1+dict.get(A[i])
    else:
        dict[A[i]]=1
sum=0
for (key,value) in dict.items():
    
    if value==B:
        sum+=key
print(sum)



