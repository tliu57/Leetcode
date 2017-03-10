from collections import defaultdict
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.count = 0

	def pathSum(self, root, sum):
		pathCount = {}
		pathCount[0] = 1
		self.dfs(root, 0, sum, pathCount)
		return self.count

	def dfs(self, node, currSum, target, pathCount):
		if not node:
			return
		currSum += node.val
		if currSum - target in pathCount:
			self.count += pathCount[currSum - target]
		if currSum not in pathCount:
			pathCount[currSum] = 1
		else:
			pathCount[currSum] += 1
		self.dfs(node.left, currSum, target, pathCount)
		self.dfs(node.right, currSum, target, pathCount)
		pathCount[currSum] -= 1


root = TreeNode(10)
node5 = TreeNode(5)
node_3 = TreeNode(-3)
node3 = TreeNode(3)
node2 = TreeNode(2)
node11 = TreeNode(11)
node32 = TreeNode(3)
node_2 = TreeNode(-2)
node1 = TreeNode(1)

root.left = node5
root.right = node_3
node5.left = node3
node5.right = node2
node_3.right = node11
node3.left = node32
node3.right = node_2
node2.right = node1

sol = Solution()
print sol.pathSum(root, 8)		

	
