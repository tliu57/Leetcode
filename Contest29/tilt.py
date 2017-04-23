class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findTilt(self, root):
		if not root:
			return 0
		left_tilt = self.findTilt(root.left)
		right_tilt = self.findTilt(root.right)
		node_tilt = abs(self.getSum(root.left) - self.getSum(root.right))
		return left_tilt + right_tilt + node_tilt

	def getSum(self, node):
		if not node:
			return 0
		return self.getSum(node.left) + self.getSum(node.right) + node.val

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
sol = Solution()
print sol.findTilt(node1)
