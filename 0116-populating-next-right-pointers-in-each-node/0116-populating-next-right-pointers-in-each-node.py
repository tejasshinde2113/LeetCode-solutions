"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=[root]
        while q:
            res=[]
            for a in range(len(q)):
                temp = q[0]

                del q[0]
                temp2 = None
                if  q:
                    temp2 = q[0]
                temp.next = temp2
                if temp.left:
                    res.append(temp.left)
                if temp.right:
                    res.append(temp.right)
            q.extend(res)
        return root

        