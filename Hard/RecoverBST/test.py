# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.n1 = None
		self.n2 = None
		self.pre = None

	def recoverTree(self, root):
	"""
	:type root: TreeNode
	:rtype: void Do not return anything, modify root in-place instead		"""	       							                    self.inorder(root)
	    if self.n1 and self.n2:						               self.n1.val, self.n2.val = self.n2.val, self.n1.val

	def inorder(self, root):
	     if not root:
		return root
	     self.inorder(root.left)
	     if not self.pre:
	     	self.pre = root
	     else:
	     	if not self.n1 and root.val < self.pre.val:
	     		self.n1 = self.pre
	     	if self.n1 and root.val < self.pre.val:
	     		self.n2 = root
	     	else:
			self.pre = root
	     self.inorder(root.right)
