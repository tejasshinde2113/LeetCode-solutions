# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head is None or k==0):
            return head
        cnt = 0
        curr = head
        while curr:
            cnt+=1
            curr = curr.next
        
        k = k%cnt

        curr = head
        temp = cnt -k
        while temp>0:
            curr = curr.next
            temp-=1
        ss = curr

        


        

        res = ListNode(0)

        res1 = res
        res1.next = ss
        temp3 = k
        while temp3>0:
            res1 = res1.next
            temp3-=1
        
        print(ss)
        temp = cnt -k
        while temp>0:
            res1.next = head
            res1 = res1.next
            head = head.next
            temp-=1 
     
        
        res1.next = None

  
        

        return res.next