class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def detectCycle(self, head):
		slow = head
		fast = head
		while True:
			if not fast or not fast.next:
				return None
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break
		slow = head
		while slow != fast:
			slow = slow.next
			fast = fast.next
		return slow

no1 = ListNode(1)
no2 = ListNode(2)
no3 = ListNode(3)
no4 = ListNode(4)
no5 = ListNode(5)
no1.next = no2
no2.next = no3
no3.next = no4
no4.next = no5
no5.next = no2

sol = Solution()
print sol.detectCycle(no1).val
