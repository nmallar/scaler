#a^n % p



class Solution:
#brute force 
    def power(self,a,n,p):
        if a==0:
            return 0   
        if n==0:
            return 1
        return (self.power(a,n-1,p) * a%p)%p
    
# #optimizedlevel1
    def optimizedLevel1Power(self,a,n,p):
        if a==0:
            return 0   
        if n==0:
            return 1
        if n%2==0:
            return (self.optimizedLevel1Power(a,n/2,p) * self.optimizedLevel1Power(a,n/2,p))%p
        else:
            return ( (self.optimizedLevel1Power(a,n/2,p) * self.optimizedLevel1Power(a,n/2,p))%p * a%p)%p
# #optimzedLevel2

    def optimizedLevel2Power(self,a,n,p):   
        if a==0:
            return 0    
        if n==0:
            return 1
        powerfun=self.optimizedLevel2Power(a,int(n/2),p)
        if n%2==0:
            return (powerfun * powerfun)%p
        else:
            return ( (powerfun * powerfun)%p * a%p)%p
        

s=Solution()
a=4
n=3
p=10
#print(s.power(a,n,p))
print(s.optimizedLevel2Power(a,n,p))