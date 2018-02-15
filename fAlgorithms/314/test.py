import collections
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def verticalOrder(self, root):
		out = []
		if not root:
			return out
		colNumber = [0]
		colMap = {}
		queue = [root]
		while queue:
			node = queue.pop(0)
			currCol = colNumber.pop(0)
			if currCol not in colMap:
				colMap[currCol] = [node.val]
			else:
				colMap[currCol].append(node.val)
			if node.left:
				queue.append(node.left)
				colNumber.append(currCol-1)
			if node.right:
				queue.append(node.right)
				colNumber.append(currCol+1)
		map = collections.OrderedDict(sorted(colMap.items()))
		for k, v in map.items():
			out.append(v)
		return out

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
print sol.verticalOrder(node3)
