# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findmid(self,head):

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None

        
        return head, sec


    def merge(self,left,right):
        final = res = ListNode()
        
        while left and right:
            if left.val <= right.val:
                res.next = left
                left= left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        
        res.next  = left or right
        return final.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head 
        first,sec = self.findmid(head)

        left =self.sortList(first)
        right = self.sortList(sec)

        return self.merge(left,right)

        