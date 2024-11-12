# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curr = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            lmax = max(left,0)
            rmax = max(right,0)

            curr[0] = max(curr[0], root.val+lmax+rmax)

            return root.val+max(lmax,rmax)
        
        dfs(root)
        return curr[0]