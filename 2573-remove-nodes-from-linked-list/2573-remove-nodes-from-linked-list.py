# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            curr = head
            prev =None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        rev = reverse(head)

        maxval = rev.val

        curr = rev

        while curr.next:
            if  curr.next and curr.next.val >= maxval:
                maxval = curr.next.val
                curr = curr.next
            else:
                curr.next = curr.next.next if curr.next.next else None
        
        

        return reverse(rev)





        