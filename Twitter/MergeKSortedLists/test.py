class ListNode(object):
    def __init__(self, x):
	self.val = x
	self.next = None

class Solution(object):
    def mergeKLists(self, lists):
	if not lists or len(lists) == 0:
		return None
	k = len(lists)
	if k == 1:
		return lists[0]
	if k == 2:
		return self.mergeTwoLists(lists[0], lists[1])
	else:
	    	return self.mergeTwoLists(self.mergeKLists[0: k/2], self.mergeKLists[k/2:])


    def mergeTwoLists(self, head1, head2):
	if not head1:
		return head2
	if not head2:
		return head1
	if head1.val < head2.val:
		head1.next = self.mergeTwoLists(head1.next, head2)
		return head1
	else:
	    	head2.next = self.mergeTwoLists(head1, head2.next)
		return head2

