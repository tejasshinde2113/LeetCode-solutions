# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque()
        q.append(root)
        cnt = 0
        while q:
            res =[]
            for a in range(len(q)):
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if cnt %2 == 0:
                    if temp.val%2 == 0:
                        return False
                    if res and (res[-1]>=temp.val ):
                        return False 
                else:
                    if temp.val%2 != 0:
                        return False
                    if res and (res[-1]<=temp.val ):
                        return False 
                res.append(temp.val)
            cnt+=1
        return True


        