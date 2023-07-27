# recursion tower of hanoi
# In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
# You have the following constraints:

# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# You have to find the solution to the Tower of Hanoi problem.
# You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
# In each row, there should be 3 integers (disk, start, end), where:

# disk - number of the disk being moved
# start - number of the tower from which the disk is being moved
# end - number of the tower to which the disk is being moved
#  input
#  A = 2
#  output 
#  [1 1 2 ] [2 1 3 ] [1 2 3 ]
#  A=3
#  [1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ] 

class Solution:
    def towerOfHanoi(self,A):
        return self.TOH(A,1,2,3)
    
    def TOH(self,N,S,T,D,lst=[]):
        
        if(N==0): 
            return lst
        self.TOH(N-1,S,D,T)
        list2=[]
        list2.append(N)
        list2.append(S)
        list2.append(D)        
        lst.append(list2)
        self.TOH(N-1,T,S,D)
        return lst
        
s=Solution()

print(s.towerOfHanoi(2))