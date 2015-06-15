from Node import ListNode

class Solution:
	def reverseList(self, head):
		curr = head
		last = None
		while curr:
			next = curr.next
			curr.next = last
			last = curr
			curr = next
		return last

