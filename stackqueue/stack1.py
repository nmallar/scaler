#implement stack using Arrays

class Stack:
    
    def __init__(self,size=10) -> None:
        self.arr=[]
        self.size=size
    
    def length(self):
        return len(self.arr)
    
    def isEmpty(self):
        return self.length() <= 0
    
    
    def pop(self):
        if not self.isEmpty():
            return self.arr.pop()
        raise Exception('Stack underflow')
    
    
    def peek(self):
        if not self.isEmpty():
             return self.arr[-1]
        raise Exception('Stack underflow')
       
    
    def push(self,num):
        
        if self.size+1 > self.length():
            self.arr.append(num)
        else:
            raise Exception("Stack overflow")
        
    def printStack(self):
        i=self.length()-1
       
        while i>=0:
            
            print(self.arr[i])
            i-=1
            
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.peek())
print(s.pop())
print(s.peek())
s.push(88)
s.printStack()