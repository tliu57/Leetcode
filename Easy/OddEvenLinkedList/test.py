class Solution()
	def oddEvenList(self, head):

		if not head or (not head.next) or (not head.next.next):
			return head

		oddindex = head
		evenindex = head.next

		while evenindex and evenindex.next:
			oddnode = evenindex.next
			evenindex.next = evenindex.next.next

			oddnode.next = oddindex.next
			oddindex.next = oddnode

			oddindex = oddindex.next
			evenindex = evenindex.next
		return head
