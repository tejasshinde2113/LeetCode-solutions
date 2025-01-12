# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,head):
        
        slow = fast= head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        temp = head
        while True:
            if temp == prev:
                temp.next = None
                break
            temp = temp.next
        return head,slow
    
    def compare(self, l1,l2):
        cur = dummyHead = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummyHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first, second = self.findMid(head)
        
        left = self.sortList(first)
        right = self.sortList(second)

        return self.compare(left,right)

        
