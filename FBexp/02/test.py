class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		carry = 0
		dummy = ListNode(-1)
		curr = dummy
		while l1 or l2 or carry:
			num1, num2 = 0, 0
			if l1:
				num1 = l1.val
				l1 = l1.next
			if l2:
				num2 = l2.val
				l2 = l2.next
			num = num1 + num2 + carry
			val = num % 10
			curr.next = ListNode(val)
			carry = num/10
			curr = curr.next
		return dummy.next

sol = Solution()
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

no1 = ListNode(5)
no6 = ListNode(6)
no4 = ListNode(4)
no1.next = no6
no6.next = no4

l1 = ListNode(5)
l2 = ListNode(5)
new_head = sol.addTwoNumbers(l1, l2)
while new_head:
	print new_head.val, "->",
	new_head = new_head.next
