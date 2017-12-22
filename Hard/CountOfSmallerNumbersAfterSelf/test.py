import sys

class SegTree(object):
    def __init__(self, start, end):
	self.start = start
	self.end = end
	self.count = 0
	self.left = None
	self.right = None

class Solution(object):
    def build(self, start, end):
	if start > end:
		return None
	root = SegTree(start, end)
	mid = (start + end)/2
	if start != end:
		root.left = self.build(start, mid)
		root.right = self.build(mid+1, end)
	else:
	    	root.count = 0
	return root

    def query(self, root, start, end):
	if start == root.start and end == root.end:
		return root.count
	mid = (root.start + root.end) / 2
	leftcount = 0
	rightcount = 0
	if root.left:
		if mid >= start and mid < end:
			leftcount = self.query(root.left, start, mid)
		else:
		    	leftcount = self.query(root.left, start, end)
	if root.right:
	      	if mid < end and mid >= start:
			rightcount = self.query(root.right, mid+1, end)
		else:
			rightcount = self.query(root.right, start, end)
	return leftcount + rightcount 
	
    def modify(self, root, index, value):
	if not root:
		return
	if root.start == index and root.end == index:
		root.count += value
		return
	mid = (root.start + root.end)/2
	if root.start <= index and index <= mid:
		self.modify(root.left, index, value)
    	if root.end >= index and index > mid:
		self.modify(root.right, index, value)
	root.count = root.left.count + root.right.count

    def countSmaller(self, nums):
	if not nums:
		return []
	root = self.build(min(nums), max(nums))
	result = []
	for i in range(len(nums)-1, -1, -1):
    	    res = self.query(root, min(nums), nums[i]-1)
	    self.modify(root, nums[i], 1)
	    result.insert(0, res)
	return result
    	
sol = Solution()
nums = [5, 2, 6, 1]
print sol.countSmaller(nums)
