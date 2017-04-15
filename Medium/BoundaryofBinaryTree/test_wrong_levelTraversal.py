class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def boundaryOfBinaryTree(self, root):
		ret = []
		if not root:
			return ret
		levels = []
		curr = [root]
		while curr:
			levels.append([node.val for node in curr])
			tmp = []
			for node in curr:
				tmp.extend([node.left, node.right])
			curr = [leaf for leaf in tmp if leaf]
		for i in range(len(levels)):
			ret.append(levels[i][0])
		for i in range(len(levels)-1, 0, -1):
			if len(levels[i]) > 1:
				ret.append(levels[i][-1])
		return ret

no1 = TreeNode(1)
no2 = TreeNode(2)
no3 = TreeNode(3)
no4 = TreeNode(4)
no1.right = no2
no2.left = no3
no2.right = no4

sol = Solution()
print sol.boundaryOfBinaryTree(no1)
