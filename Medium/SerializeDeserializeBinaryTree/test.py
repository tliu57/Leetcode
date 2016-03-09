
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Codec:
	def serialize(self, root):
		ret_str = ''
		if not root:
			ret_str = ',None'
			return ret_str
		ret_str += ',' + str(root.val)
		ret_str += self.serialize(root.left)
		ret_str += self.serialize(root.right)
		return ret_str

	def deserialize(self, data):
		data = data[1:].split(",")
		data_list = []
		for elem in data:
			if elem == "None":
				data_list.append(None)
			else:
				data_list.append(int(elem))
		root, count =  self.buildTree(data_list, -1)
		return root

	def buildTree(self, data, pos):
		print "----------------------"
		pos += 1
		if pos >= len(data) or data[pos] == None:
			return None, pos
		root = TreeNode(data[pos])
		root.left, pos = self.buildTree(data, pos)
		if root.left:
			print "root.left.val is:", root.left.val
		print "pos is", pos
		root.right, pos = self.buildTree(data, pos)
		if root.right:
			print "root.right.val is:", root.right.val
		print "pos is", pos
		print "-----------------------"
		return root, pos
		
n20 = TreeNode(20)
n8 = TreeNode(8)
n4 = TreeNode(4)
n12 = TreeNode(12)
n10 = TreeNode(10)
n14 = TreeNode(14)
n22 = TreeNode(22)
n20.left = n8
n20.right = n22
n8.left = n4
n8.right = n12
n12.left = n10
n12.right = n14

codec = Codec()
serial =  codec.serialize(n20)
print serial
root =  codec.deserialize(serial)
#print root.val
left =  root.left
#print left.val
#print left.left.val
#print left.right.val
#print left.right.left.val
#print left.right.right.val
