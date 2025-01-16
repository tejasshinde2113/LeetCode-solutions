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
        

        def dfs(root, path):
            if not root.left and not root.right:
                res.append(path)
            
            dfs(root.left, path + '->' + str(root.left.val)) if root.left else None
            dfs(root.right, path + '->' + str(root.right.val)) if root.right else None
            
        dfs(root,str(root.val))
        return res