class TreeLinkNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	def connect(self, root):
		head = None
		prev = None
		curr = root
		while curr:
			while curr:
				if curr.left:
					if prev:
						prev.next = curr.left
					else:
						head = curr.left
					prev = curr.left
				if curr.right:
					if prev:
						prev.next = curr.right
					else:
						head = curr.right
					prev = curr.right
				curr = curr.next
			curr = head
			prev = None
			head = None
		return root
	
no1 = TreeLinkNode(1)
no2 = TreeLinkNode(2)
no3 = TreeLinkNode(3)
no4 = TreeLinkNode(4)
no5 = TreeLinkNode(5)
no6 = TreeLinkNode(6)
no7 = TreeLinkNode(7)
no1.left = no2
no1.right = no3
no2.left = no4
no2.right = no5
no3.left = no6
no3.right = no7
sol = Solution()
no1 = sol.connect(no1)
def visit(node):
	while node:
		print "node.val:", node.val,
		node = node.next
	print "\n"
head = no1
queue = [head]
while queue:
	head = queue.pop()
	visit(head)	
	if head.left:
		queue.insert(0, head.left)
	elif head.right:
		queue.insert(0, head.right)


