class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		if not nums or len(nums) == 0:
			return None
		root = self.buildTree(0, len(nums)-1, nums)
		return root

	def buildTree(self, start, end, nums):
		if start > end:
			return None
		elif start == end:
			return TreeNode(nums[start])
		else:
			mid = end - (end - start) / 2
			node = TreeNode(nums[mid])
			node.left = self.buildTree(start, mid - 1, nums)
			node.right = self.buildTree(mid + 1, end, nums)
			return node

sol = Solution()
print sol.sortedArrayToBST([1, 2, 3, 4])
