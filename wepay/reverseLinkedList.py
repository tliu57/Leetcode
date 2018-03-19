class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		prev = None
		curr = head
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev

sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
new_head = sol.reverseList(node1)
ptr = new_head
while ptr:
	print(ptr.val),
	ptr = ptr.next
