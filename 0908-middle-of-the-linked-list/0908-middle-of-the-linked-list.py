# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.ne
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
       
        while fast and fast.next:
     
            slow = slow.next
            fast = fast.next.next
     
        return slow
        