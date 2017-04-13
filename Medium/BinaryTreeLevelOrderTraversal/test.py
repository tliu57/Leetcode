class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self, root):
		ret = []
		if not root:
			return ret
		curr = [root]
		while curr:
			ret.append([node.val for node in curr])
			tmp = []
			for node in curr:
				tmp.extend([node.left, node.right])
			curr = [leaf for leaf in tmp if leaf]		
		
		return ret

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

sol = Solution()
print sol.levelOrder(node3)
