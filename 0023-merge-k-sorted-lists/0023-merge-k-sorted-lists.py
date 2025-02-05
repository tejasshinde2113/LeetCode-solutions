# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]

        for a in lists:

            curr =a
            while curr:
                heap.append(curr.val)
                curr=curr.next
        
        heapq.heapify(heap)
        
        res = ListNode()
        curr = res

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return res.next 

        