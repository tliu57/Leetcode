class ListNode(object):
    def __init__(self, x):
	self.val = x
	self.next = None

    def mergeKLists(self, lists):
	dummy = ListNode(-1)
	pointer = dummy
	k = len(lists)
	h = [(n.val, n) for n in lists if n]
	heapify(h)
    	while h:
		value, node = heappop()
    		if node.next:
    			heapreplace(h, (node.next.val, node.next))
    		else:
		    	heappop(h)
		pointer.next = node
		pointer = pointer.next
	return dummy.next
