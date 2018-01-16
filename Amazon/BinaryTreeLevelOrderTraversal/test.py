class TreeNode():
    def __init__(self, x):
	self.val = x
	self.left = None
	self.right = None

class Solution():
    def levelOrder(self, root):
	result = []
	q = [root]
	while q:
		result.append([node.val for node in q])
		next_q = []
		for node in q:
			if node.left:
				next_q.append(node.left)
			if node.right:
				next_q.append(node.right)
		q = next_q
	return result

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
node2.left = TreeNode(4)
sol = Solution()
print sol.levelOrder(root)
