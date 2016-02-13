class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def longestConsecutive(self, root):

		return len(self.dfs(root))

	def dfs(self, root):
		if not root:
			return []
	
		left_list = self.dfs(root.left)
		if left_list != [] and root.val == left_list[0] - 1:
			left_list.insert(0, root.val)
		elif left_list == []:
			left_list.append(root.val)
	
		right_list = self.dfs(root.right)
		if right_list != [] and root.val == right_list[0] - 1:
			right_list.insert(0, root.val)
		elif right_list == []:
			right_list.append(root.val)
		if len(left_list) > len(right_list):
			return left_list
		else:
		 	return right_list

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node2.right = node4
node4.left = node3
node4.right = node5

sol = Solution()
print sol.longestConsecutive(node1)
