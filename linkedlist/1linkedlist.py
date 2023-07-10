class Node:
    def __init__(self,data) -> None:
        
        self.data=data 
        self.next=None
        
    def size(self,head):
        
        temp=head
        count=0
        while(temp!=None):
            
            temp=temp.next 
            count+=1
        return count
    
    def printLinkedList(self, node):
        temp=node
        while(temp!=None):
            print(f" {temp.data} ",end= " ")
            temp=temp.next 
            
    def insertAtK(self, head, position,value):
        if position>self.size(head):
            return head
        newnode=Node(value)
        newnode.next=None
         
        if position==0:
            newnode.next=head.next 
            head=newnode
            return head
        
        temp=head
        count=1
        while(temp!=None and count<position-1):
            temp=temp.next 
            count+=1
       
        newnode.next=temp.next 
        temp.next=newnode
        return head    
        
        
    def deleteAtK(self,head,position):
        if position >  self.size(head):
            return head
        temp=head
        if position==1:
            head=head.next 
            return head
        
        count=1
        while count<position-1:
              temp=temp.next 
              count+=1
        temp.next =(temp.next).next
        return head
            

head=Node(10)
temp = head
for i in range(20,60,10):
    temp.next=Node(i)
    temp=temp.next
    
print(head.size(head))
head.printLinkedList(head)
head=head.insertAtK(head,5,67)
print()
head.printLinkedList(head)
head=head.deleteAtK(head,1)
print()
head.printLinkedList(head)

     