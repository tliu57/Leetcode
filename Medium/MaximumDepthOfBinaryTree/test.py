class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if not root:
			return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

sol = Solution()
node1 = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(8)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4

print sol.maxDepth(node1)
