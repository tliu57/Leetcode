class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		return self.reverseListHelper(head, None)

	def reverseListHelper(self, head, prev):
		if not head:
			return prev
		nxtNode = head.next
		head.next = prev
		return self.reverseListHelper(nxtNode, head)		


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
node = sol.reverseList(l1)
while node:
	print node.val, "->",
	node = node.next
