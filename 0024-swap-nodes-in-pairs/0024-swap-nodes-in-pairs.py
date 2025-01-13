# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        res = prev = ListNode(0)

        while curr and curr.next:
            temp = curr.next.next
            swap1 = curr.next

            swap1.next = curr
            curr.next = temp

            prev.next = swap1
            prev = curr
            curr = temp

        return res.next
        