# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt =0
        curr = head
        while curr:
            cnt+=1
            curr = curr.next
        it = cnt-n
    

        curr = head
        i = 0

        if(cnt==1):
            return head.next

        while curr:
            if cnt-n==1:
                curr.next = curr.next.next
                cnt-=1
            elif(cnt==n):
                return head.next
            else:
                curr = curr.next
            cnt-=1

        return head