
# # We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.

# Shaggy wants you to find a special pair such that the distance between that pair is minimum. 
# Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

#A = [7, 1, 3, 4, 1, 7]
A=[1, 1]

dict={}
min_len=len(A)+1

for i in range(len(A)):
    if A[i] in dict:
        min_len=min(min_len,i-dict.get(A[i]))
    else:
        dict[A[i]]=i

if min_len==len(A)+1:
    print(-1)
else:
    print(min_len)