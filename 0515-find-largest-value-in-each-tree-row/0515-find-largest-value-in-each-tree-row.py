# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        final =[]
        q=[root]

        while q:
            comp = -2**31 -1
            for a in range(len(q)):
                temp = q[0]
                del q[0]

                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                comp = max(comp,temp.val)
            final.append(comp)
        return final
        