# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def sorted(final, lst):
            temp  = ListNode()
            ret = temp
            while final and lst:
                if final.val > lst.val:
                    temp.next = ListNode(lst.val)
                    lst = lst.next
                else:
                    temp.next = ListNode(final.val)
                    final = final.next
                temp = temp.next
            
            temp.next = lst or final
            return ret.next



        final = None
        for a in lists:
            if a:
                final = sorted(final,a)
            
        return final
        