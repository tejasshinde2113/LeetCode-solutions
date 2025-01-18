# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        res = 0

        q = deque([(root,root.val,root.val)])

        while q:
            temp = q.popleft()

            res = max(abs(temp[1]-temp[2]), res)


            if temp[0].left:
                q.append((temp[0].left, max(temp[1],temp[0].val,temp[0].left.val), 
                                        min(temp[2],temp[0].val,temp[0].left.val)))
            if temp[0].right:
                q.append((temp[0].right, max(temp[1],temp[0].val,temp[0].right.val), 
                                         min(temp[2],temp[0].val,temp[0].right.val)))
        return res

        