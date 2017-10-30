class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class Solution(object):
	def __init__(self):
		self.map = {}

	def dfs(self, node):
		if node is None:
			return 0
		d = max(self.dfs(node.left), self.dfs(node.right)) + 1
		if d not in self.map:
			self.map[d] = []
		self.map[d].append(node.val)
		return d

	def findLeaves(self, root):
		maxDepth = self.dfs(root)
		res = []
		for i in range(1, maxDepth+1):
			res.append(self.map[i])
		return res
		

node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2
node1.right = TreeNode(3)
node2.left = TreeNode(4)
node2.right = TreeNode(5)

sol = Solution()
print sol.findLeaves(node1)
		
