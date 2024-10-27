# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=[root]
        final = []
        if not root:
            return 0
        while q:
            res = []
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                res.append(temp.val)
            final.append(res)
        return final[-1][0]
        