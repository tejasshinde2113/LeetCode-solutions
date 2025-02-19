# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            fast=fast.next.next
            slow = slow.next
        
        
        prev.next = None

        curr = slow
        rev = None

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        

        curr = head
        while rev:

            temp = curr.next if curr.next else None

            curr.next = rev
            curr = curr.next
            rev = rev.next
            if temp:
                curr.next = temp
                curr = curr.next
            else:
                break
        
        return head






        
        