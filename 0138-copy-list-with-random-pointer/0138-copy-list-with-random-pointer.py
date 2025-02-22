"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        

        dct ={None: None}
        curr = head
        
        while curr:
            temp = Node(curr.val)
            dct[curr] = temp
            curr = curr.next
        

        curr = head

        while curr:
            newnode = dct[curr]

            newnode.next = dct[curr.next]
            newnode.random = dct[curr.random]

            curr = curr.next

        return dct[head]