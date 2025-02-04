# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        temp = res = ListNode(0)
        cnt = 0
        while l1 and l2:
            add = l1.val + l2.val + cnt
            if add >9:
                cnt=1
            else:
                cnt=0
            add = add%10

            temp.next = ListNode(add)

            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        l3 = l1 or l2
        

        
        while l3:

            add = l3.val + cnt
            if add >9:
                cnt=1
            else:
                cnt=0
            add = add%10

            temp.next = ListNode(add)

            temp = temp.next
            l3 = l3.next  

        if cnt:
            temp.next = ListNode(1)
        return res.next

            
        