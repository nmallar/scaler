# advance recursion

# tower oh hanoi

#approach move first N-1 discs from source S to temporary T
# move Nth disc from source to destination S to D

class Solution:
    
    def TOH(self,N,S,T,D):
        if(N==0): 
            return
        self.TOH(N-1,S,D,T)
        print(f"{N} : {S} to {D}")
        self.TOH(N-1,T,S,D)
s=Solution()
s.TOH(3,'Source','Temp','Destination')
