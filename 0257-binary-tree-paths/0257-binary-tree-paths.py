# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        q = deque([[root, str(root.val)]])

        while q:

            temp ,path= q.popleft()

            if not temp.left and not temp.right:
                res.append(path)
            
            if temp.left:
                q.append([temp.left, path+'->'+str(temp.left.val)])
            if temp.right:
                q.append([temp.right, path+'->'+str(temp.right.val)])
        return res



        

        return res
        