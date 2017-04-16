class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.ret = []
	
	def boundaryOfBinaryTree(self, root):
		if not root:
			return self.ret
		self.ret.append(root.val)
		self.leftBoundary(root.left)
		self.leaves(root.left)
		self.leaves(root.right)
		self.rightBoundary(root.right)
		return self.ret

	def leftBoundary(self, node):
		# return left boundary of all internal nodes
		if not node or (not node.left and not node.right):
			return
		self.ret.append(node.val)
		if not node.left:
			self.leftBoundary(node.right)
		else:
			self.leftBoundary(node.left)
	
	def rightBoundary(self, node):
		# return right boundary of all internal nodes
		if not node or (not node.left and not node.right):
			return
		if not node.right:
			self.rightBoundary(node.left)
		else:
			self.rightBoundary(node.right)
		self.ret.append(node.val)

	def leaves(self, node):
		if not node:
			return
		if not node.left and not node.right:
			self.ret.append(node.val)
			return
		self.leaves(node.left)
		self.leaves(node.right)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

sol = Solution()
print sol.boundaryOfBinaryTree(root)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)
print sol.boundaryOfBinaryTree(root)
