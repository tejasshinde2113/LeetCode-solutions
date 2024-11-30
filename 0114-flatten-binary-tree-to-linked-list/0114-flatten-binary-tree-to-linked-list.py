# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        q=[root]
        while q:
            temp =q.pop()
            
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)
            if q:
                temp.right = q[-1]
            temp.left = None
                
        
        