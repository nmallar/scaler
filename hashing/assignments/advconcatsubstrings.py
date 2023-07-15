#advancedhashing
#Problem Description
#Given a string B, find if it is possible to re-order the characters of the string B so that it can be represented as a concatenation of A similar strings.
#Eg: B = aabb and A = 2, then it is possible to re-arrange the string as "abab" which is a concatenation of 2 similar strings "ab".
#If it is possible, return 1, else return -1.

#Approach
# Each character must come in multiples of A if we are to represent the string as a concatenation of A strings.
# Why?Because that count divided by A will the number of times that particular character appears in 1 string.
# So we maintain a hash which stores the frequency of each character.
# Then we iterate over the hash and check if each character that appeared in the array appeared as a mutiple of A or not.
# If there exists even 1 character whose hash[i] % A is not equal to 0, it implies we cannot represent the string as A concatenated strings
# Else the answer is yes.

class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dict={}
        for i in range(len(B)):
            dict[B[i]]=1+dict.get(B[i],0)
        for key in dict:
            if dict[key]%A!=0:
                return -1
        return 1

s=Solution()
A=2
B="bbaabb"  
print(s.solve(A,B))          
    