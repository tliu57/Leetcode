class Solution(object):
	def largestBSTSubtree(self, root):
		def dfs(root):
			if not root:
				return 0, 0, float('inf'), float('-inf')
			N1, n1, min1, max1 = dfs(root.left)
			print "N1 is:", N1, "n1 is:", n1, "min1", min1, "max1", max1
			N2, n2, min2, max2 = dfs(root.right)
			print "N2 is:", N2, "n2 is:", n2, "min2", min2, "max2", max2
			n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
			print "n is:", n
			return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
		return dfs(root)[0]

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

node10 = TreeNode(10)
node5 = TreeNode(5)
node1 = TreeNode(1)
node8 = TreeNode(8)
node15 = TreeNode(15)
node7 = TreeNode(7)
node10.left = node5
node5.left = node1
node5.right = node8
node10.right = node15
node15.right = node7

sol = Solution()
print sol.largestBSTSubtree(node10)
