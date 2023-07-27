#advance recursion
#fibonacci
# fib number     1 2 3 4 5 6 7 8  9  10 11
#              0 1 1 2 3 5 8 13 21 34 55

class Solution:
    
    def fib(self,n):
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        

s=Solution()
n=1
print(s.fib(n))