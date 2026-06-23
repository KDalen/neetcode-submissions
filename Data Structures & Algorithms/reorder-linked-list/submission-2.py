# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        #reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
       
        #merge
        first, second = head, prev
        while second:
            print(first.val, second.val)
            temp = first.next
            temp2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2
            

