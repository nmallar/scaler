#Binsray Search Tree: All left nodes are smaller than root and all on right are larger that right.
# same applies to each subtree


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
    
    def searchBST(self,root,k):
        
        while root!=None:
            if root.data==k:
                return True
            elif root.data < k:
                root=root.right
            elif root.data > k:
                root=root.left
        return False
    
    def isSimilar(self,root1,root2):
        if root1==None and root2==None:
            return True
        if (root1!=None and root2==None) or (root2!=None and root1==None):
            return False
        if root1.data==root2.data and self.isSimilar(root1.left,root2.left) and self.isSimilar(root1.right,root2.right):
            return True
    
        
        
    def height(self,root):
        if root==None:
            return 0
        heightLeft=self.height(root.left)
        heightRight=self.height(root.right)
        
        return max(heightLeft,heightRight)+1
    
    
    def isBalancedTree(self,root):
        isBalanced=True
        height2(root)
        
    def height2(self,root,isBalance):
        if root==None:
            return 0
        heightLeft=self.height(root.left)
        heightRight=self.height(root.right)
        if abs(heightLeft-heightRight)>1:
            isBalance=False
        return max(heightLeft,heightRight)+1
        
    
root=Node(12)
root.left=Node(7)
root.right=Node(25)
root.left.left=Node(6)
root.left.right=Node(9)
root.right.left=Node(20)
root.right.right=Node(30)


root.inorder(root)
# root.invert(root)
# root.inorder(root)
#print(root.searchBST(root,30))
 
print()
root2=Node(12)
root2.left=Node(7)
root2.right=Node(25)
root2.left.left=Node(6)
root2.left.right=Node(9)
root2.right.left=Node(20)
root2.right.right=Node(30)
root2.inorder(root)
print(root.isSimilar(root,root2))