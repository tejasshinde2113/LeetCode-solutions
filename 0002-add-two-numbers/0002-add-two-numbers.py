# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev,prev2=l1,l2

        res = ListNode(0)

        res2 = res
        carry=0

        while prev or prev2:
            val1,val2=0,0

            if(prev !=None):
                val1 = prev.val
                prev = prev.next
            if(prev2 != None):
                val2 = prev2.val
                prev2 = prev2.next
            
            final = (val1+val2+carry)%10
            carry = (val1+val2+carry)//10

            res2.next = ListNode(final)
            res2 = res2.next
        
        if(carry>0):
            res2.next = ListNode(carry)
            res2 = res2.next

        return res.next

        
        
        