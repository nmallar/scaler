#invert tree.. left becomes right ..right become left
class Node:
    
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    
    def invert(self,root):
    
        if root==None:
            return
        self.invert(root.left)
        self.invert(root.right)
    
        temp=root.left
        root.left=root.right
        root.right=temp
        
    
    
    
root=Node(10)
root.left=Node(20)
root.right=Node(30)

root.inorder(root)
root.invert(root)
root.inorder(root)
 