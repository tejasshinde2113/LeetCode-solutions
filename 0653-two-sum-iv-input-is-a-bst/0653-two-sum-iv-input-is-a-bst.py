# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        q=[root]
        d = dict()
        while q:
            for a in range(len(q)):
                temp =q[0]
                del q[0]
                if k - temp.val in d:
                    return True
                d[temp.val] = 1
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
        return False



        

        