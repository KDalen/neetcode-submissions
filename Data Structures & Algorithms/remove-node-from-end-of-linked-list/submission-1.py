# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        for i in range(n):
            f = f.next
        prev, curr = None, head
        while f:
    
            
            f=f.next
            prev = curr
            curr = curr.next

        if prev is None:
            return head.next
        prev.next = curr.next
        return head
