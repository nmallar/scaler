# advanced hashing 1
# Problem Description
# Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
# Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dict={}
        mindistance=len(A)
        for i in range(len(A)):
            if A[i] in dict:
                if i-dict[A[i]]<mindistance:
                    mindistance=i-dict[A[i]]
                    dict[A[i]]=i
            else:
                dict[A[i]]=i
        if mindistance==len(A):
            return -1
        else:
            return mindistance
        
            
        



s=Solution()
#A=[7, 1, 3, 4, 1, 7]
A=[1,1]

print(s.solve(A))          