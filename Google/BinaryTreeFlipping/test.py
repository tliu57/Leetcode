class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def __init__(self):
		self.new_root = None

	def upsideDownBinaryTree(self, root):
		if root:
			self.dfs(root)
		return self.new_root

	def dfs(self, root):
		if not root.left:
			self.new_root = root
			return
		left_node = root.left
		right_node = root.right
		self.dfs(left_node)
		left_node.right = root
		left_node.left = right_node
		root.left = None
		root.right = None

orig_tree = TreeNode(1)
left_sub = TreeNode(2)
orig_tree.right = TreeNode(3)
orig_tree.left = left_sub
left_sub.left = TreeNode(4)
left_sub.right = TreeNode(5)

sol = Solution()
new_node = sol.upsideDownBinaryTree(orig_tree)
q = [new_node]
# q = [orig_tree]
print "xxx, new_node.val:{}".format(new_node.val)

def levelOrder(root):
	ret = []
        if not root:
                return ret
        curr = [root]
        while curr:
                ret.append([node.val for node in curr])
                tmp = []
                for node in curr:
                        tmp.extend([node.left, node.right])
                curr = [leaf for leaf in tmp if leaf]

        return ret
print levelOrder(new_node)
