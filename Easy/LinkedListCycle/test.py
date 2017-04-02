class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):
		try:
			slow = head
			fast = head.next
			while slow != fast:
				slow = slow.next
				fast = fast.next.next
			return True
		except:
			return False

no0= ListNode(0)
no1 = ListNode(1)
no2 = ListNode(2)
no3 = ListNode(3)
no0.next = no1
no1.next = no3
no3.next = no2
no2.next = no3

sol = Solution()
print sol.hasCycle(no0)
