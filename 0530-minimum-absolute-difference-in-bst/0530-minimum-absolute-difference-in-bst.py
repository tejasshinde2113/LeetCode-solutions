# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        res = []
        def sort(root):
            if not root:
                return 
            
            sort(root.left)
            res.append(root.val)
            sort(root.right)
        
        sort(root)
        m = 10**5+1
        for a in range(1,len(res)):
            m = min(m, abs(res[a]-res[a-1]))
        return m