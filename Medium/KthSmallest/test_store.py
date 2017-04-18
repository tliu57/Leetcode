class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution():
	def kthSmallest(self, root, k):
		count = []
		self.storeToList(root, count)
		return count[k-1]

	def storeToList(self, node, count):
		if not node:
			return
		self.storeToList(node.left, count)
		count.append(node.val)
		self.storeToList(node.right, count)

root = TreeNode(3)
no6 = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.right = no6
no6.right = TreeNode(7)
no6.left = TreeNode(5)

sol = Solution()
print sol.kthSmallest(root, 2)


