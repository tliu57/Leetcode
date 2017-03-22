class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		stack1 = []
		stack2 = []
		
		while l1:
			stack1.append(l1.val)
			l1 = l1.next

		while l2:
			stack2.append(l2.val)
			l2 = l2.next
		
		sum = 0
		list = ListNode(0)
		while stack1 or stack2:
			sum += stack1.pop() if stack1 else 0
			sum += stack2.pop() if stack2 else 0
			list.val = sum % 10
			head = ListNode(sum/10)
			head.next = list
			sum /= 10
			list = head
		
		return list if list.val != 0 else list.next


l1 = ListNode(7)
l3 = ListNode(2)
l5 = ListNode(4)
l7 = ListNode(3)

l2 = ListNode(5)
l4 = ListNode(6)
l6 = ListNode(4)

l1.next = l3
l3.next = l5
l5.next = l7

l2.next = l4
l4.next = l6

sol = Solution()
node = sol.addTwoNumbers(l1, l2)
print "node.val:", node.val
while node:
	print node.val, "->"
	node = node.next	
		
			
