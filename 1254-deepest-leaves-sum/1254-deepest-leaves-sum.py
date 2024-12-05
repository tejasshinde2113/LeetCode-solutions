# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        res=[]
        while q:
            k =0
            for a in range(len(q)):
                temp = q[0]
                del q[0]

                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                k+=temp.val
            res.append(k)
        return res[-1]