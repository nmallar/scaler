
# Given an array A of integers and another non negative integer B .
#Find if there exists 2 indices i and j such that A[i] - A[j] = B and i != j.
#edge case difference is zero .. handle both positive and negative

class Solution:
    def diffPossible(self, A,B):
       
        dict={}
        
        for i in range(0,len(A)):
            ans=B+A[i]
            if A[i] in dict:
                return 1
            elif ans not in dict:
                    dict[ans]=i
        
       
        
        return 0
        
    def diffPossible2(self,A,B):
                
        dict=set()
        for i in range(len(A)):
            a=A[i]
            ans1=A[i]-B
            ans2=A[i]+B
            if ans1 in dict or ans2 in dict:
               
                return 1
            else:
                 
                dict.add(a)
        return 0 
                        
s=Solution()

#A=[2,3,4,5,6,7,8]
#A=[4,7,-4,2,2,2,3,-5,-3,9,-4,9,-7,7,-1,9,9,4,1,-4,-2,3,-3,-5,4,-7,7,9,-4,4,-8]
#A=[77,28,19,21,67,15,53,25,82,52,8,94,50,30,37,39,9,43,35,48,82,53,16,20,13,95,18,67,77,12,93,0]
#A=[0]
#A=[11,85,100,44,3,32,96,72,93,76,67,93,63,5,10,45,99,35,13]
#B=60
#A=[77,28,19,21,67,15,53,25,82,543,8,94,50,30,37,39,9,43,35,48,82,53,16,20,13,95,18,67,77,12,93,0]
#A=[53,28,19,0]
#B=53
A=[34,63,64,38,65,83,50,44,18,34,71,80,22,28,20,96,33,70,0,25,64,96,18,2,53,100,24,47,98,69,60,55,8,38,72,94,18,68,0,53,18,30,86,55,13,93,15,43,73,68,29]
B=97
print(A)
print(f"B is {B}")
# print(s.diffPossible(A,B))


print(s.diffPossible2(A,B))