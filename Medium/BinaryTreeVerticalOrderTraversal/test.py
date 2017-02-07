import collections

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def verticalOrder(self, root):
		verticalOrder = []
		if not root:
			return verticalOrder
		queue = [root]
		colNumber = [0]
		colMap = {}
		while queue:
			currNode = queue.pop(0)
			currCol = colNumber.pop(0)
			if currCol not in colMap:
				colMap[currCol] = [currNode.val]
			else:
				colMap[currCol].append(currNode.val)
			if currNode.left:
				queue.append(currNode.left)
				colNumber.append(currCol-1)
			if currNode.right:
				queue.append(currNode.right)
				colNumber.append(currCol+1)
		colMap = collections.OrderedDict(sorted(colMap.items()))
		for k, v in colMap.items():
			verticalOrder.append(v)
		return verticalOrder


node3 = TreeNode(3)
node9 = TreeNode(9)
node8 = TreeNode(8)
node4 = TreeNode(4)
node0 = TreeNode(0)
node1 = TreeNode(1)
node7 = TreeNode(7)
node3.left = node9
node3.right = node8
node9.left = node4
node9.right = node0
node8.left = node1
node8.right = node7
sol = Solution()
print sol.verticalOrder(node3) 
			
			
