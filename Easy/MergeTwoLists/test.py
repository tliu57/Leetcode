class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1
		result = ListNode(0)
		pointer = result
		while l1 and l2:
			if l1.val < l2.val:
				pointer.next = l1
				l1 = l1.next
			else:
				pointer.next = l2
				l2 = l2.next
			pointer = pointer.next
		if l1:
			pointer.next = l1
		if l2:
			pointer.next = l2

		return result.next

l1 = ListNode(1)
l13 = ListNode(3)
l15 = ListNode(5)

l2 = ListNode(2)
l24 = ListNode(4)
l26 = ListNode(6)

l1.next = l13
l13.next = l15

l2.next = l24
l24.next = l26

sol = Solution()
pointer = sol.mergeTwoLists(l1, l2)
while pointer:
	print pointer.val, "->",
	pointer = pointer.next
