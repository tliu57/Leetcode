class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def __init__(self):
		self.sum = 0
	
	def dfs(self, node):
		if not node:
			return
		self.dfs(node.right)
		self.sum += node.val
		node.val = self.sum
		self.dfs(node.left)

	def convertBST(self, root):
		self.dfs(root)
		return root

sol = Solution()
orig_tree = TreeNode(5)
orig_tree.left = TreeNode(2)
orig_tree.right = TreeNode(13)

new_root = sol.convertBST(orig_tree)
print new_root.val
if new_root.left:
	print new_root.left.val
if new_root.right:
	print new_root.right.val

