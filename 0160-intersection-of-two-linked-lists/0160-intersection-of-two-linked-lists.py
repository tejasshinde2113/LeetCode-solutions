# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        cntB ,cntA=0,0

        while B:
            cntB+=1
            B = B.next

        while A:
            cntA+=1
            A = A.next

        A = headA
        B = headB
        if cntA>cntB:
            temp = cntA-cntB
            while temp>0:
                temp-=1
                A = A.next
        elif cntA<cntB:
            temp = cntB-cntA
            while temp>0:
                temp-=1
                B = B.next


        while A and B:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None



















        