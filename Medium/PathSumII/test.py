class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		if not root:
			return []
		if not root.left and not root.right and root.val == sum:
			return [[root.val]]
		sum -= root.val
		prev_list = self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
		return [[root.val] + i for i in prev_list]

node5 = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node7 = TreeNode(7)
node2 = TreeNode(2)
node13 = TreeNode(13)
node42 = TreeNode(4)
node52 = TreeNode(5)
node1 = TreeNode(1)


node5.left = node4
node5.right = node8
node4.left = node11
node11.left = node7
node11.right = node2
node8.left = node13
node8.right = node4
node4.left = node52
node4.right = node1


testRoot = TreeNode(3)
test2 = TreeNode(2)
test1 = TreeNode(1)
test1_1 = TreeNode(1)
testRoot.left = test2
testRoot.right = test1
test1.right = test1_1

sol = Solution()
sum = 22
print sol.pathSum(testRoot, 5)


