class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		dummy = ListNode(-1)
		dummy.next = head
		curr = dummy
		nxt = dummy.next
		while nxt:
			while nxt.next and nxt.next.val == nxt.val:
				nxt = nxt.next
			if curr.next != nxt:
				curr.next = nxt.next
			else:
				curr = curr.next
			nxt = nxt.next
		return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

sol = Solution()
new_head = sol.deleteDuplicates(node1)
ptr = new_head
while ptr:
	print ptr.val, "->",
	ptr = ptr.next 
