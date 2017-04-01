class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome(self, head):
		slow, fast = head, head
		stack = []
		while fast and fast.next:
			stack.append(slow.val)
			slow = slow.next
			fast = fast.next.next
		if fast:
			slow = slow.next
		while slow.next:
			if slow.val == stack[-1]:
				slow = slow.next
				stack.pop()
			else:
				return False
		if slow.val != stack.pop():
			return False
		return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)
node1.next = node2
node2.next = node3

no1 = ListNode(1)
no2 = ListNode(2)
no3 = ListNode(2)
no4 = ListNode(1)
no1.next = no2
no2.next = no3
no3.next = no4

sol = Solution()
print sol.isPalindrome(no1)
print sol.isPalindrome(node1)

