import sys
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isValidBST(self, root):
		if not root:
			return True
		return self.validateBSTHelper(root, -sys.maxint, sys.maxint)

	def validateBSTHelper(self, root, min, max):
		if not root:
			return True
		if root.val <= min or root.val >= max:
			return False
		return self.validateBSTHelper(root.left, min, root.val) and self.validateBSTHelper(root.right, root.val, max)

node2 = TreeNode(2)
node1 = TreeNode(1)
node3 = TreeNode(3)
node2.left = node1
node2.right = node3

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node1.left = Node2
Node1.right = Node3

sol = Solution()
print sol.isValidBST(node2)
print sol.isValidBST(Node1)
