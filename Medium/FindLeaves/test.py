class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution():
	def findLeaves(self, root):
		res = []
		self.height(root, res)
		return res

	def height(self, node, res):
		if not node:
			return -1
		level = 1 + max(self.height(node.left, res), self.height(node.right, res))
		if len(res) < level + 1:
			res.append([])
		res[level].append(node.val)
		return level


rootNode = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node5 = TreeNode(5)

rootNode.left = Node2
rootNode.right = Node3
Node2.left = Node4
Node2.right = Node5

sol = Solution()
print sol.findLeaves(rootNode)
