# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res=[0]

        def dfs(root,comp):
            if not root:
                return
            
            if root.val >= comp:
                res[0] = res[0]+1
            maxi = max(root.val,comp)
            dfs(root.left,maxi)
            dfs(root.right,maxi)

        dfs(root,root.val-1)
        return res[0]

        # res =0
        
        # q=deque([(root,root.val -1)])

        # while q:

        #     temp,comp= q.popleft()

        #     if temp.val >= comp:
        #         res+=1
        #     maxi = max(temp.val,comp)
        #     if temp.left:
        #         q.append((temp.left,maxi ))
        #     if temp.right:
        #         q.append((temp.right, maxi))
        # return res




        