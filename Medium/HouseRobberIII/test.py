class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rob(self, root):
		res = self.robHelper(root)
		return max(res[0], res[1])

	def robHelper(self, node):
		if not node:
			return [0]* 2
		left_list = self.robHelper(node.left)
		right_list = self.robHelper(node.right)

		robMoney = [0]* 2
		# first element stands for node house not being robbed, second element stands for house being robbed
		robMoney[0] = max(left_list[0], left_list[1]) + max(right_list[0], right_list[1])
		robMoney[1] = node.val + left_list[0] + right_list[0]
		return robMoney 
		


tree_root = TreeNode(3)
left_first = TreeNode(2)
right_first = TreeNode(3)
left_second = TreeNode(3)
right_second = TreeNode(1)
tree_root.left = left_first
tree_root.right = right_first
left_first.right = left_second
right_first.right = right_second

sol = Solution()
print sol.rob(tree_root)		
