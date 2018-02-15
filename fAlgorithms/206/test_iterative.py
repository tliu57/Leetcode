class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseLinkedList(self, head):
		prev = None
		curr = head
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt 
		return prev

no1 = ListNode(1)
no2 = ListNode(2)
no1.next = no2
sol = Solution()
newhead = sol.reverseLinkedList(no1)
ptr = newhead
while ptr:
	print ptr.val, '->',
	ptr = ptr.next
