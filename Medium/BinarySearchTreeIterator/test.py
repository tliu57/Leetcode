class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

node8 = TreeNode(8)
node3 = TreeNode(3)
node1 = TreeNode(1)
node6 = TreeNode(6)
node4 = TreeNode(4)
node7 = TreeNode(7)
node10 = TreeNode(10)
node14 = TreeNode(14)
node13 = TreeNode(13)

node8.left = node3
node3.left = node1
node3.right = node6
node6.left = node4
node6.right = node7
node8.right = node10
node10.right = node14
node14.left = node13

class BSTIterator(object):
	def __init__(self, root):
		self.stack = []
		self.setRoot(root)

	def hasNext(self):
		return self.stack !=[]

	def next(self):
		if not self.stack:
			return -1
		node = self.stack.pop()
		val = node.val
		self.setRoot(node.right)
		return val

	def setRoot(self, node):
		while node:
			self.stack.append(node)
			node = node.left

i = BSTIterator(node8)
v = []
while i.hasNext():
	v.append(i.next())
	print v
