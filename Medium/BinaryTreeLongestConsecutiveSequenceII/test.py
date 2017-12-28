class TreeNode(object):
    def __init__(self, x):
	self.val = x
	self.left = None
	self.right = None

class Solution(object):
    def __init__(self):
	self.max = 0

    def longestConsecutive(self, root):
	self.dfs(root)
	return self.max

    def dfs(self, node):
	if not node:
		return 0, 0
	inc = 1
	dec = 1
	if node.left:
		left_inc, left_dec = self.dfs(node.left)
		if node.val == node.left.val + 1:
			inc = left_inc + 1
		elif node.val == node.left.val -1:
			dec = left_dec + 1

	if node.right:
		right_inc, right_dec = self.dfs(node.right)
    		if node.val == node.right.val + 1:
			inc = max(inc, right_inc + 1)
    		elif node.val == node.right.val - 1:
			dec = max(dec, right_dec + 1)
	self.max = max(self.max, inc+dec-1)
    	return inc, dec

sol = Solution()
root = TreeNode(3)
left = TreeNode(1)
right = TreeNode(2)
root.left = left
left.right = right
right.left = TreeNode(4)
right.left.left = TreeNode(5)
print sol.longestConsecutive(root)
