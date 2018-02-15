import sys
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def __init__(self):
		self.maxSubtreeNode = None
		self.maxSum = -sys.maxint

	def findSubtree(self, root):
		maxSum = self.dfs(root)
		return self.maxSubtreeNode

	def dfs(self, node):
		if not node:
			return 0
		left_sum = self.dfs(node.left)
		right_sum = self.dfs(node.right)
		if self.maxSum == 0 or node.val + left_sum + right_sum > self.maxSum:
			self.maxSum = node.val + left_sum + right_sum
			self.maxSubtreeNode = node
		return node.val + left_sum + right_sum

orig_node = TreeNode(1)
left_node = TreeNode(-5)
right_node = TreeNode(2)
orig_node.left = left_node
orig_node.right = right_node
left_node.left = TreeNode(0)
left_node.right = TreeNode(3)
right_node.left = TreeNode(-4)
right_node.right = TreeNode(-5)

sol = Solution()
print sol.findSubtree(orig_node).val

