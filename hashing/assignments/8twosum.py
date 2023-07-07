# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. 
# Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array 
# and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.
# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

class Solution:
    def twoSum(self, A,B):
        print(A)
        dict={}
        
        for i in range(0,len(A)):
            ans=B-A[i]
            if A[i] in dict:
                return [dict[A[i]]+1,i+1]
            elif ans not in dict:
                    dict[ans]=i      
        
        return []
        
        
                
s=Solution()

#A=[2,3,4,5,6,7,8]
A=[4,7,-4,2,2,2,3,-5,-3,9,-4,9,-7,7,-1,9,9,4,1,-4,-2,3,-3,-5,4,-7,7,9,-4,4,-8]
B=-3

print(s.twoSum(A,B))