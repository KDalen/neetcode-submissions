
class Solution:
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next and slow:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False