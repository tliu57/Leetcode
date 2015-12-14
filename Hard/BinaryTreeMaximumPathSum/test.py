from sys import maxint
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def maxPathSum(self, root):
		res = -maxint
		self.maxPathSumUtil(root, res)
		return res

	def maxPathSumUtil(self, root, res):
		if not root:
			return 0
		leftSum = self.maxPathSumUtil(root.left, res)
		print "leftSum is: %d"%leftSum,
		rightSum = self.maxPathSumUtil(root.right, res)
		print "rightSum is: %d"%rightSum,
		singleSum = max(root.val, root.val + max(leftSum, rightSum)) 
		print "root.val is :%d"%root.val
		currentSum = max(singleSum, leftSum + root.val + rightSum)
	      	print "before, res is:", res
		res = max(res, currentSum)
		print "then, res is:", res
	      	print "---------------------"
		return singleSum
	
root =  TreeNode(1)
node1 = TreeNode(-2)
node2 = TreeNode(-3)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(-2)
node6 = TreeNode(-1)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node3.left = node6
solution = Solution()
print solution.maxPathSum(root)
