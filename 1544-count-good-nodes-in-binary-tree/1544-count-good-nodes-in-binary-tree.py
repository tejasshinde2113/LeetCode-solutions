# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res =0
        if not root:
            return res
        q=deque([(root,root.val -1)])

        while q:

            temp,comp= q.popleft()

            if temp.val >= comp:
                res+=1
            
            if temp.left:
                q.append((temp.left, max(temp.val,comp)))
            if temp.right:
                q.append((temp.right, max(temp.val,comp)))
        return res




        