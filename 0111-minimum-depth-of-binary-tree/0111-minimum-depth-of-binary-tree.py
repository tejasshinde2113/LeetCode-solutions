# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        q=[root]
        cnt=0

        while q:
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                
                if not(temp.left or temp.right):
                  
                    return cnt+1
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
           
            cnt+=1
         
        
            
        
