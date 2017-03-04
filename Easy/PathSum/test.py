class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def hasPathSum(self, root, sum):
		if not root:
			return False
		if not root.left and not root.right and root.val == sum:
			return True
		sum -= root.val
		return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

node5 = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node7 = TreeNode(7)
node2 = TreeNode(2)
node13 = TreeNode(13)
node42 = TreeNode(4)
node1 = TreeNode(1)

node5.left = node4
node5.right = node8
node4.left = node11
node11.left = node7
node11.right = node2
node8.left = node13
node8.right = node42
node42.right = node1

sol = Solution()
print sol.hasPathSum(node5, 22)
