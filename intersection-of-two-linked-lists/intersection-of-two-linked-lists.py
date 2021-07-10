# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return
        a = headA; b=headB; l1=0;l2=0
        def length(head):
            x = 0
            while head:
                x+=1;head=head.next
            return x
        l1 = length(a)
        l2 = length(b)
        a = headA; b=headB;
        if l1>l2:
            for i in range(l1-l2): a=a.next
        else:
            for k in range(l2-l1): b=b.next
        while a and b:
            if a==b: return a
            else:
                a=a.next;b=b.next
        return 
            
                
       
            
        