# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        cnt =0
        while q:
            res = []
            for a in range(len(q)):
                temp = q.popleft()
                res.append(temp)   
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
            
            if cnt%2==1:
                p1=0
                p2=len(res)-1
                while p1<=p2:
                    k = res[p1].val 
                    res[p1].val = res[p2].val
                    res[p2].val = k
                    p1+=1
                    p2-=1
            cnt+=1

        return root

                
                    
            