# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        stack=[]
        list=[]
        while A != None:
            list.append(A.val) 
            stack.append(A)           
            A=A.left
        
        while len(stack) > 0:
            A=stack.pop()
             
            if A.right != None:            
                A=A.right
                while A != None:
                    stack.append(A)
                    list.append(A.val) 
                    A=A.left      

        return list