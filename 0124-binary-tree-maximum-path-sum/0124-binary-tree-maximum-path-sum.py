# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [-1001]

        def dfs(root):
            if not root:
                return 0
            

            left = dfs(root.left)
            right = dfs(root.right)
            lmax = max(left,0)
            rmax = max(right,0)
            res[0] = max(res[0], lmax+rmax+root.val)

            return root.val+ max(lmax,rmax)
        dfs(root)
        return res[0]
        