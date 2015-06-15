from solution import Solution
from Node import ListNode

testCase = Solution()

Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node1.next = Node2
Node2.next = Node3

print testCase.reverseList(Node1).val
print Node3.next.val
print Node2.next.val
