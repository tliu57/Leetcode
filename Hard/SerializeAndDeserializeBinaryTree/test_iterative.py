class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec:
	
	def serialize(self, root):
		if not root:
			return ''
		queue = [root]
		idx = 0
		while idx < len(queue):
			if queue[idx] is not None:
				queue.append(queue[idx].left)
				queue.append(queue[idx].right)
			idx += 1
		return ",".join([str(node.val) if node else "#" for node in queue])

	def deserialize(self, data):
		if data == '':
			return None
		data = data.split(",")
		root = TreeNode(data[0])
		queue = [root]
		isLeftnode = True
		idx = 0
		for val in data[1:]:
			if val != "#":
				node = TreeNode(int(val))
				if isLeftnode:
					queue[idx].left = node
				else:
					queue[idx].right = node
				queue.append(node)
			if not isLeftnode:
				idx += 1
			isLeftnode = not isLeftnode
		return root


no1 = TreeNode(1)
no2 = TreeNode(2)
no3 = TreeNode(3)
no4 = TreeNode(4)
no5 = TreeNode(5)
no1.left = no2
no1.right = no3
no3.left = no4
no3.right = no5


code = Codec()
string =  code.serialize(no1)
print string
new_root = code.deserialize(string)
print code.serialize(new_root)
