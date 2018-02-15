from heapq import heapify, heappop, heapreplace
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		dummy = ListNode(-1)
		curr = dummy
		h = [(n.val, n) for n in lists if n]
		heapify(h)
		while h:
			value, node = h[0]
			if not node.next:
				heappop(h)
			else:
				heapreplace(h, (node.next.val, node.next))
			curr.next = node
			curr = curr.next
		return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

nod1 = ListNode(4)
nod2 = ListNode(5)
nod3 = ListNode(6)
nod1.next = nod2
nod2.next = nod3

node_lists = [node1, nod1]
sol = Solution()
no = sol.mergeKLists(node_lists)
while no:
	print no.val, "->"
	no = no.next
			
