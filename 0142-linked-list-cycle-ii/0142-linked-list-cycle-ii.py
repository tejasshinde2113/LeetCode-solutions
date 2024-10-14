# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        slow = head
        fast = head.next
        temp = head
        s = set()
        while slow:
            if slow in s:
                return slow
            s.add(slow)
            slow = slow.next            


        return None
        