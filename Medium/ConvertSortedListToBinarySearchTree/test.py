class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedListToBST(self, head):
		if not head:
			return None
		root = self.buildTree(head, None)
		return root

	def buildTree(self, head, tail):
		if head == tail:
			return None
		slow = head
		fast = head
		while fast!= tail and fast.next != tail:
			slow = slow.next
			fast = fast.next.next
		node = TreeNode(slow.val)
		node.left = self.buildTree(head, slow)
		node.right = self.buildTree(slow.next, tail)
		return node

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
print sol.sortedListToBST(head)
		
