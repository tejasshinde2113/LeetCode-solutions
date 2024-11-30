# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        prev=None
        def dfs(root):
            nonlocal prev 
            if not root:
                return 
            
            dfs(root.right)
            dfs(root.left)

            root.right = prev
            root.left = None
            prev = root
        dfs(root)
        