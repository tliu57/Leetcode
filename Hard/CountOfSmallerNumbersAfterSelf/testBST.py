class Node(object):
    def __init__(self, value):
	self.left = None
	self.right = None
	self.val = value
	self.count = 1
	self.leftTreeSize = 0

class BinarySearchTree(object):
    def __init__(self):
	self.root = None

    def insert(self, val, root):
	if not root:
		self.root = Node(val)
		return 0

	if val == root.val:
		root.count += 1
		return root.leftTreeSize

	if val < root.val:
		root.leftTreeSize += 1
		if not root.left:
			root.left = Node(val)
    			return 0
		return self.insert(val, root.left)
    	
    	if not root.right:
		root.right = Node(val)
    		return root.count + root.leftTreeSize

	return root.count + root.leftTreeSize + self.insert(val, root.right)

class Solution(object):
    def countSmaller(self, nums):
	tree = BinarySearchTree()
	result = []
	for i in range(len(nums)-1, -1, -1):
		res = tree.insert(nums[i], tree.root)
		result.insert(0, res)
	return result

sol = Solution()
print sol.countSmaller([5, 2, 6, 1])



