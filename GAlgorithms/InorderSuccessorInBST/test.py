class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def inorderSuccessor(self, root, p):
		return self.dfs(root, p)

	def dfs(self, root, p):
		if not root:
			return None
		if p.val < root.val:
			if root.left and self.dfs(root.left, p):
				return self.dfs(root.left, p)
			return root
		else:
			return self.dfs(root.right, p)

sol = Solution()
first_tree = TreeNode(2)
first_tree.left = TreeNode(1)

print sol.inorderSuccessor(first_tree, TreeNode(1)).val

second_tree = TreeNode(2)
second_tree.left = TreeNode(1)
second_tree.right = TreeNode(3)
print sol.inorderSuccessor(second_tree, TreeNode(2)).val
