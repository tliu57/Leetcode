class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		if not root:
			return True
		left_height = self.getHeight(root.left)
		right_height = self.getHeight(root.right)
		if abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
			return True
		return False

	def getHeight(self, node):
		if not node:
			return 0
		return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

no50 = TreeNode(50)
no17 = TreeNode(17)
no76 = TreeNode(76)
no9 = TreeNode(9)
no23 = TreeNode(23)
no50.left = no17
no50.right = no76
no17.left = no9
no17.right = no23
no9.right = TreeNode(14)
no9.right.left = TreeNode(12)
no23.left = TreeNode(19)
no76.left = TreeNode(54)
no76.left.right = TreeNode(72)
no76.left.right.left = TreeNode(67)

sol = Solution()
print sol.isBalanced(no50)
		
