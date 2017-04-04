class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec:
	def serialize(self, root):
		ret = ""
		if not root:
			ret += ",None"
			return ret
		else:
			ret += "," + str(root.val)
			ret += self.serialize(root.left)
			ret += self.serialize(root.right)
			return ret

	def deserialize(self, data):
		data = data[1:].split(",")
		list = []
		for elem in data:
			if elem == "None":
				list.append(None)
			else:
				list.append(int(elem))
		root, count = self.buildTree(list, -1)
		return root

	def buildTree(self, list, pos):
		pos += 1
		if pos >= len(list) or list[pos] == None:
			return None, pos
		node = TreeNode(list[pos])
		node.left, pos = self.buildTree(list, pos)
		node.right, pos = self.buildTree(list, pos)
		return node, pos



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

codec = Codec()
string = codec.serialize(node1)
node = codec.deserialize(string)
print codec.serialize(node)
