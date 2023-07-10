#Given a root node of a binary tree,
# we cannot change node structure


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
    
    def preorder(self,root):
        if root==None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
       
    
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
    
    def size(self,root):
        if root==None:
            return 0
        l=self.size(root.left)
        r=self.size(root.right)
        return r+l+1
        
    def sum(self,root):
        if root==None:
            return 0
        lsum=self.sum(root.left)
        rsum=self.sum(root.right)
        return lsum+rsum+root.data
        
    
    def height(self,root):
        if root==None:
            return 0
        hl=self.height(root.left)
        hr=self.height(root.right)
        return max(hl,lr)+1   
        
root=Node(10)
root.left=Node(20)
root.right=Node(30)
