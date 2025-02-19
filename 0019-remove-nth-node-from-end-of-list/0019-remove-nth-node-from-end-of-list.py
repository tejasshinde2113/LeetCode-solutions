# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cnt=0
        curr = head
        
        while curr:
            curr = curr.next
            cnt+=1

        
        cnt = cnt -n

        if cnt ==0:
            return head.next
            

        curr = head
        while cnt >1:
            curr = curr.next
            cnt-=1

        temp = curr.next.next if curr.next.next else None
        curr.next = temp
        return head

        
        