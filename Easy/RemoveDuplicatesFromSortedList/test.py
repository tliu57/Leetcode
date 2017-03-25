class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		curr = head
		while curr:
			while curr.next and curr.val == curr.next.val:
				curr.next = curr.next.next
			curr = curr.next
		return head

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
node = sol.deleteDuplicates(node1)
while node:
	print node.val, "->",
	node = node.next
