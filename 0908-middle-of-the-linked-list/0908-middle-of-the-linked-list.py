# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.ne
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        temp = l//2
        while temp>0:
            temp-=1
            head = head.next
        return head
        