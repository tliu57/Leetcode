class TreeNode(object):
    def __init__(self, x):
	self.val = x
	self.left = None
	self.right = None

class Solution(object):
    def findTarget(self, root, k):
	dic = {}
	out = self.dfs(root, dic, k)
	return out

    def dfs(self, node, dic, target):
	if not node:
		return False
	if target - node.val in dic:
		return True
	else:
		dic[node.val] = node
		return self.dfs(node.left, dic, target) or self.dfs(node.right, dic, target)



sol = Solution()
root = TreeNode(5)
left1 = TreeNode(3)
right1 = TreeNode(6)
left2 = TreeNode(2)
right2 = TreeNode(7)
root.left = left1
root.right = right1
right1.right = right2
left1.left = left2
left1.right = TreeNode(4)
print sol.findTarget(root, 9)
