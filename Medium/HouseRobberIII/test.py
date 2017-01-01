class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rob(self, root):
		return self.robHelper(root, dict())

	def robHelper(self, node, map):
		if not node:
			return 0
		if node in map.keys():
			return map[node]

		robMoney = 0
		if node.left:
			robMoney += self.robHelper(node.left.left, map) + self.robHelper(node.left.right, map)
		if node.right:
			robMoney += self.robHelper(node.right.left, map) + self.robHelper(node.right.right, map)
		value = max(robMoney + node.val, self.robHelper(node.left, map) + self.robHelper(node.right, map))
		map[node] = value
		return value 
		


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
