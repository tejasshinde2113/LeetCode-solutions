# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next:
            return head.val
        k = 0
        
        

        slow = fast =head

        while fast and fast.next:
            k+=1
            slow = slow.next
            fast = fast.next.next
        
        
        start = head
        res = [0]*(k)
        first = 0
        last = k -1
        while slow:
            res[first] += start.val
            res[last] += slow.val
            first +=1
            last-=1
            slow=slow.next
            start = start.next
        
        return max(res)
            


