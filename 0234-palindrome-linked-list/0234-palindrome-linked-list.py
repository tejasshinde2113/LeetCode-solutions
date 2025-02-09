# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow=fast = head

        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        new = prev.next
        prev.next = None

        rev = None
        while new:
            temp = new.next
            new.next = rev
            rev = new
            new = temp
        
        while head:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True


