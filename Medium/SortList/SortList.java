/**
 * Created by TianranLiu on 2/22/15.
 */
public class Solution {
    public ListNode sortList(ListNode head) 
    {
	   if(head == null || head.next == null) return head;
	    ListNode end = head;
	    while(end.next != null) {
	    	end = end.next;
	    }
	    head = mergeSort(head, end);
	    return head;

    }

    private ListNode mergeSort(ListNode begin, ListNode end){
    	    if(begin == end) return begin;
	    ListNode slow = begin;
	    ListNode fast = begin;
	    while(fast != end){
		fast = fast.next;
		if(fast != end) {
			slow = slow.next;
			fast = fast.next;
		}
	    }

	    ListNode slowNext = slow.next;
	    slow.next = null;
	    ListNode pointer1 = mergeSort(begin, slow);
	    ListNode pointer2 = mergeSort(slowNext, fast);

	    ListNode pre = new ListNode(Integer.MIN_VALUE);
	    ListNode pointer = pre;
	    
	    while(pointer1 != null && pointer2 != null){
		if(pointer1.val < pointer2.val){
			pointer.next = pointer1;
			pointer1 = pointer1.next;	
		}
		else{
			pointer.next = pointer2;
			pointer2 = pointer2.next;
		}
		pointer = pointer.next;

       	}
	    if(pointer1 != null) pointer.next = pointer1;
	    if(pointer2 != null) pointer.next = pointer2;

	return pre.next;


    }
}
