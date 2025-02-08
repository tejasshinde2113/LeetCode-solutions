# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res =[-1001]

        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            lmax = max(left,0)
            rmax = max(right,0)
            res[0] = max(res[0],node.val + lmax+rmax)

            return node.val + max(lmax,rmax)
        check(root)
        return res[0]
        

        

        