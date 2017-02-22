class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		ans = 0
		if not root:
			return ans
		if root.left:
			if not root.left.left and not root.left.right:
				ans += root.left.val
			else:
				ans += self.sumOfLeftLeaves(root.left)
		ans += self.sumOfLeftLeaves(root.right)
		return ans



root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
root.left = node9
root.right = node20
node20.left = node15
node20.right = node7

sol = Solution()
print sol.sumOfLeftLeaves(root)		
