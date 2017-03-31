class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		stack = []
		res = []
		if not root:
			return res
		stack.append(root)
		while stack:
			node = stack.pop()
			res.append(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return res[::-1]

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

sol = Solution()
print sol.postorderTraversal(node1)
