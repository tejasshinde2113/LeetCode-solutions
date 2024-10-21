# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     
        q=[root]
        cnt =0
        if root is None:
            return 0
        while q:
            length = len(q)
            for a in range(length):
                temp = q[0]
                del q[0]
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
            cnt+=1
        return cnt
        