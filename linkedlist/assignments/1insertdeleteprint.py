#Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and a pointer to the next node.
# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).

# input : First line contains an integer denoting number of cases, let's say t. Next t line denotes the cases.

# output When there is a case of print_ll(), Print the entire linked list, such that each element is followed by a single space.

# There should not be any trailing space.
#pending correction

class Node:
    def __init__(self,data) -> None:
        
        self.data=data 
        self.next=None
        
class LinkedList:
    
    def __init__(self) -> None:
         self.head=None
         
    def size(self,node):
        
        temp=node
        count=0
        while(temp!=None):
            
            temp=temp.next 
            count+=1
        return count

    def insert_node(self,position, value):
        # @param position, an integer
        # @param value, an integer
           
            newnode=Node(value)
            newnode.next=None
            
            if position==1 :
                newnode.next=self.head.next 
                self.head=newnode
                return self.head
            
            temp=self.head
            count=1
            while(temp!=None and count<position-1 and count<self.size(self.head)):
                temp=temp.next 
                count+=1
        
            newnode.next=temp.next 
            temp.next=newnode
            return self.head


    def delete_node(self,position):
        # @param position, integer
        # @return an integer
            if position >  self.size(self.head)+1:
                return self.head
            temp=self.head
            if position==1:
                self.head=self.head.next 
                return  self.head
            
            count=1
            while count<position-1:
                temp=temp.next 
                count+=1
            temp.next =(temp.next).next
            return self.head

    def print_ll(self):
        # Output each element followed by a space
            temp=self.head
            while(temp!=None):
                print(f"{temp.data}",end= " ")
                temp=temp.next
            print() 


linkedListObj = LinkedList()
numOfcases=int(input())
dict={}
i=0
while i<numOfcases:
    lst =input().split()
    dict[i]=lst
    i+=1
j=0
while j<i:
    command=dict[j]     
     
    if command[0]=='i':
        if linkedListObj.head==None:  
            linkedListObj.head=Node(int(command[2]))
        else:
            linkedListObj.head=linkedListObj.insert_node(int(command[1]),int(command[2]))
    elif command[0]=='p':
        linkedListObj.print_ll()
    elif command[0]=='d':
        linkedListObj.head=linkedListObj.delete_node(int(command[1]))
    j+=1        
       

