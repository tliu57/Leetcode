class SegmentTree(object):
    def __init__(self, start, end, sum=0):
	self.start = start
	self.end = end
	self.sum = sum
	self.left, self.right = None, None

    @classmethod
    def build(cls, start, end, array):
	if start > end:
		return None
	if start == end:
		return SegmentTree(start, end, array[start])

	node = SegmentTree(start, end)
	mid = (start + end) / 2
	node.left = cls.build(start, mid, array)
    	node.right = cls.build(mid+1, end, array)
    	node.sum = node.left.sum + node.right.sum
	return node

    @classmethod
    def modify(cls, root, index, value):
	if root is None:
		return
	if root.start == root.end:
		root.sum = value
		return
	if root.left.end >= index:
		cls.modify(root.left, index, value)
	else:
	    	cls.modify(root.right, index, value)
	root.sum = root.left.sum + root.right.sum
 
    @classmethod
    def query(cls, root, start, end):
	if root.start > end or root.end < start:
		return 0
	if start <= root.start and root.end <= end:
		return root.sum
	return cls.query(root.left, start, end) + cls.query(root.right, start, end)


class Solution():
    def __init__(self, A):
	self.root= SegmentTree.build(0, len(A)-1, A)

    def query(self, start, end):
	return SegmentTree.query(self.root, start, end)

    def modify(self, index, value):
	SegmentTree.modify(self.root, index, value)
	

sol = Solution([1, 2, 7, 8, 5])
print sol.query(0, 2)
print sol.modify(0, 4)
print sol.query(0, 1)
print sol.modify(2, 1)
print sol.query(2, 4)
