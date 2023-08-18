class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):

        len_A=len(A)
        len_B=len(B)
        
        if len_A == 1 and len_B==1:
            if A[0] =='1' and B[0]=='1':
                return '10'
            else:
                return str(int(A[0])+int(B[0]))
            
        str_A=A
        str_B=B
        diff=len_A-len_B
        if diff>0:
            length=len(str_A)
            str_B=("0"*diff)+str_B
             
        else:
            length=len(str_B)
            diff=diff*-1
            str_A=("0"*diff)+str_A
            

     
        ans=""
        
        sum=0
        for i in range(length-1,-1,-1):            
            bitsum=sum+int(str_A[i])+int(str_B[i])
            r=bitsum%2
            ans+=str(r)
            sum=bitsum//2
        
        if sum==1:
            ans+='1'
        return ans[::-1]


s=Solution()

#print(s.addBinary('1010110111001101101000','1000011011000000111100110'))

print(s.addBinary('11','1'))