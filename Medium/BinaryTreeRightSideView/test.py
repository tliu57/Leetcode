class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rightSideView(self, root):
		ret = []
		if not root:
			return ret
		curr = [root]
		while curr:
			ret.append(curr[-1].val)
			tmp = []
			for node in curr:
				tmp.extend([node.left, node.right])
			curr = [leaf for leaf in tmp if leaf]
		return ret

no1 = TreeNode(1)
no2 = TreeNode(2)
no3 = TreeNode(3)
no5 = TreeNode(5)
no4 = TreeNode(4)

no1.left = no2
no1.right = no3
no2.right = no5
no3.right = no4

sol = Solution()
print sol.rightSideView(no1)			
		
