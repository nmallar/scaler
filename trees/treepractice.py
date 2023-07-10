# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
		#list=[]
		if A==None:
			return list
		self.inorderTraversal(A.left)
		print(A.val)
		self.inorderTraversal(A.right)
       
		
     
		

A=[1,3,2]
s=Solution()
print(s.inorderTraversal(A))