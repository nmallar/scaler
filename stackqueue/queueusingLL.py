#queue using LL



class Node:
    def __init__(self,data) -> None:
        
        self.data=data 
        self.next=None       
        
        
class Queue:
    
    def __init__(self) -> None:        
        self.front=None
        self.rear=None
        self.count=0
        
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.rear==None
    
    def insert(self,data):
        newnode=Node(data)
        if self.front==None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
        
    
    def delete(self):
        if not self.isEmpty():
            node=self.front
            self.front=self.front.next
            return node.data
        raise Exception("Queue is empty")
    
    def rear(self):
        pass
        
    def front(self):
        pass
    
    def printQueue(self):
        temp=self.front
        while temp!=None:
            print(temp.data)
            temp=temp.next 
    
q1=Queue()

q1.insert(10)
q1.insert(20)
q1.insert(30)
q1.insert(40)

q1.insert(50)
q1.insert(60)
q1.printQueue()
q1.delete()
q1.printQueue()
        
        