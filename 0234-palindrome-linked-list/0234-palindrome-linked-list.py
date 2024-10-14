# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt = 0
        curr = head

        while curr:
            cnt+=1
            curr = curr.next
        
        temp =round(cnt/2)
        curr = head
        while temp>0:
            curr = curr.next
            temp-=1
        
        curr2 = curr
        prev=None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        
        
        cnt=cnt//2
        start = head
        while cnt>0:
            if(prev.val != start.val):
                
                return False
            prev = prev.next
            start = start.next
            cnt-=1
        return True
        