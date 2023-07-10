#implement stack using linkedlist

class Node:
    def __init__(self,data) -> None:
        
        self.data=data 
        self.next=None       
        
        
class Stack:
    
    def __init__(self) -> None:        
        self.head=None
        self.count=0
        
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.head==None
        
    def push(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
            
        self.count+=1                        
    
    def pop(self):
        if self.head==None:
            raise Exception("Underflow")
        self.head=self.head.next
        self.count-=1
    
    def peek(self):
        if self.head==None:
            raise Exception("Stack Empty")
        return self.head.data
        
    def print(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
        
        
st=Stack()

st.push(2)
st.push(3)
st.push(4)
st.push(5)

st.pop()
st.print()


st.pop()
print(st.peek())