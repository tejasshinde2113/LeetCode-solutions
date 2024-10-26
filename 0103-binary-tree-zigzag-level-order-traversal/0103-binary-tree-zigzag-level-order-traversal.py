# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [] 

        q= [root]
        final = []
        flag = False
        while q:
            res =[]
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                

                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
               
                
                res.append(temp.val)
            final.append(res)

        
        return [a  if i%2==0 else a[::-1]  for i, a in enumerate(final)]


        