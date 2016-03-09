#		6
#	      /	  \
#           2       7
#         /   \       \
#        1     4       9
#             /  \    /
#            3    5  8
#
# Preorder: 6 2 1 4 3 5 7 9 8
# Inorder: 1 2 3 4 5 6 7 8 9


class TreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution():
	def buildTree(self, preorder, inorder):
		if not preorder or len(preorder)==0:
			return None
		if len(preorder) != len(inorder):
			return None
		return self.buildTreeHelper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

	def buildTreeHelper(self, preorder, inorder, preorder_index, preorder_end, inorder_index, inorder_end):
		if preorder_index > preorder_end or inorder_index > inorder_end:
			return None
		root_val = preorder[preorder_index]
		root = TreeNode(root_val)
		if preorder_index == preorder_end or inorder_index == inorder_end:
			return root
		ii = inorder_index
		while inorder[ii] != root_val:
			ii += 1
		left_subtree_size = ii - inorder_index
		root.left = self.buildTreeHelper(preorder, inorder, preorder_index + 1, preorder_index + left_subtree_size, inorder_index, inorder_index + left_subtree_size)
		root.right = self.buildTreeHelper(preorder, inorder, preorder_index + left_subtree_size + 1, preorder_end, ii+1, inorder_end)
		return root

preorder = [6, 2, 1, 4, 3, 5, 7, 9, 8]
inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sol = Solution()
print sol.buildTree(preorder, inorder).val
