class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def kthSmallest(self, root, k):
		left_count = self.countNodes(root.left)
		if left_count >= k:
			return self.kthSmallest(root.left, k)
		elif left_count+1< k:
			return self.kthSmallest(root.right, k-left_count-1 )
		return root.val

	def countNodes(self, node):
		if not node:
			return 0
		return 1 + self.countNodes(node.left) + self.countNodes(node.right)

node7 = TreeNode(7)
node5 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node6 = TreeNode(6)
node10 = TreeNode(10)
node9 = TreeNode(9)
node12 = TreeNode(12)
node13 = TreeNode(13)
node7.left = node5
node5.left = node3
node5.right = node6
node3.right = node4
node7.right = node10
node10.left = node9
node10.right = node12
node12.right = node13

sol = Solution()
print sol.kthSmallest(node7, 4)
