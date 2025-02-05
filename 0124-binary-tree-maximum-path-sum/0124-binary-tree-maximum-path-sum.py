# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-1001]

        def m(node):
            if not node:
                return 0



            left = m(node.left)
            leftmax = max(0,left)

            right = m(node.right)
            rightmax = max(0,right)

            res[0]=max(res[0],node.val+leftmax+rightmax)

            return node.val + max(leftmax,rightmax)

        (m(root))
        return res[0]
        

        

        