# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[[root,0]]
        maxval = 0

        while q:
            res=[]
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                
                if temp[0].left:
                    q.append([temp[0].left,temp[1]*2])
                if temp[0].right:
                    q.append([temp[0].right,temp[1]*2 + 1])
                res.append(temp[1])
            maxval = max(maxval,res[-1]-res[0]+1)
        return maxval