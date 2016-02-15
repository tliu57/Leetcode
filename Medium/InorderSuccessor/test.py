class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderSuccessor(self, root, p):
		if not root:
			return None
		if root.val > p.val:
			return self.inorderSuccessor(root.left, p) or root
		else:
			return self.inorderSuccessor(root.right, p)

	def leftMostNode(self, root):
		node = root
		while node.left:
			node = node.left
		return node

node1 = TreeNode(1)
node3 = TreeNode(3)
node8 = TreeNode(8)
node6 = TreeNode(6)
node4 = TreeNode(4)
node7 = TreeNode(7)
node10 = TreeNode(10)
node14 = TreeNode(14)
node13 = TreeNode(13)
node8.left = node3
node8.right = node10
node10.right = node14
node14.left = node13
node3.left = node1
node3.right = node6
node6.left = node4
node6.right = node7

sol = Solution()
print sol.inorderSuccessor(node8, node3).val
