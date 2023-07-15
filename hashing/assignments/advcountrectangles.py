#advanced hashing : count rectangles
# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.
# Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) 
# form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.



from collections import OrderedDict


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        od=OrderedDict()
        for i in range(len(A)):
            od[(A[i],B[i])]=1 
        
        count=0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                (x1,y1)=A[i],B[i]
                (x2,y2)=A[j],B[j]
                
                if x1==x2 or y1==y2:
                    continue
                if (x2,y1) in od and (x1,y2) in od:
                    count=count+1
        return int(count/2) 


A = [1, 1, 2, 2]
B = [1, 2, 1, 2]

s=Solution()
print(s.solve(A,B))

