class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution():
	def __init__(self):
		self.max = 0
	
	def longestConsecutiveSequence(self, root):
		if not root:
			return 0
		self.helper(root, 0, root.val)
		return self.max
	
	def helper(self, root, cur, target):
		if not root:
			return
		if root.val == target:
			cur += 1
		else:
			cur = 1
		self.max = max(self.max, cur)
		self.helper(root.left, cur, root.val + 1)
		self.helper(root.right, cur, root.val + 1)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.right = node3


sol = Solution()
print sol.longestConsecutiveSequence(node1)


