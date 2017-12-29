class TreeNode(object):
    def __init__(self, x):
	self.val = x
	self.left = None
	self.right = None

class Solution(object):
    def __init__(self):
	self.max = 0

    def longestUnivaluePath(self, root):
	self.dfs(root)
	return self.max

    def dfs(self, node):
	if not node:
		return 0
	left = 0
	right = 0
	if node.left:
		left = self.dfs(node.left)
		if node.val == node.left.val:
			left += 1
	if node.right:
		right = self.dfs(node.right)
		if node.val == node.right.val:
			right += 1
	self.max = max(self.max, left+right)
	return max(left, right)

sol = Solution()
root = TreeNode(1)
left1 = TreeNode(4)
right1 = TreeNode(5)
left2 = TreeNode(4)
right2 = TreeNode(5)
root.left = left1
root.right = right1
left1.left = left2
right1.right = right2
left1.right = TreeNode(4)
print sol.longestUnivaluePath(root)
