#Subarray with given sum
# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single integer "-1".
# First sub-array means the sub-array for which starting index in minimum.
#hint: two pointer approach


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    
    #sub optimal appraoch
    # def solve(self, A, B):          
       
    #     slow=0
    #     fast=0
    #     while  slow<len(A):
    #         sum=A[slow]
    #         if sum==B:
    #             return [A[slow]]
    #         sum=0
    #         while(fast<len(A)):                
    #             sum+=A[fast]
    #             #print(f"sum is {sum}")                
    #             if sum==B:
    #                 li=[]
    #                 for i in range(slow,fast+1):
    #                     li.append(A[i])
    #                 return li
    #             fast=fast+1
    #         slow+=1
    #         fast=slow         
                
    #     return [-1]

    def add(self,A, left,right):
        sum=0
        while(left<=right and left<len(A) and right<len(A)):
            sum+=A[left]
            left+=1
        return sum


    def twoSum(self, A,B):
        
        dict={}
        dict[0]=-1
        sum=0
        s=-1
        e=-1
        for i in range(0,len(A)):
            sum+=A[i]
            ans=sum-B
            if ans in dict:
                return [A[j] for j in range(dict[ans]+1,i+1)]
            else:
                    dict[sum]=i      
        
        return [-1]
        
        
                
s=Solution()
#A=[2,4,3,8,3]
#A=[1,2,3,4,5]
#A=[42,9,38,36,48,33,36,50,38,8,13,37,33,38,17,25,50,50,41,29,34,18,16,6,49,16,21,29,41,7,37,14,5,30,35,26,38,35,9,36,34,39,9,4,41,40,3,50,27,17,14,5,31,42,5,39,38,38,47,24,41,5,50,9,29,14,19,27,6,23,17,1,22,38,35,6,35,41,34,21,30,45,48,45,37]
#A=[1,2,3,4,5]
A=[5,10,20,100,105]
B=240
print(A)

print(s.twoSum(A,B))