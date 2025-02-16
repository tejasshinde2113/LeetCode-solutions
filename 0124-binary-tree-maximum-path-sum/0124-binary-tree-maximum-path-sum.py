# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res =[-1001]
        
        def path(root):
            if not root:
                return 0
            
            left = path(root.left)
            right = path(root.right)

            lmax = max(left,0)
            rmax  = max(right,0)

            res[0] = max(res[0],root.val+lmax+rmax)
            return root.val+max(lmax,rmax)

        

        path(root)
        return res[0]
        

