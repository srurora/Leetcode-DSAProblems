# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        if not l1: return l2
        if not l2: return l1
        if l1.val<l2.val:
            dummy.next = l1
            dummy.next.next=self.mergeTwoLists(l1.next,l2)
        else:
            dummy.next = l2
            dummy.next.next=self.mergeTwoLists(l1,l2.next)
        return dummy.next