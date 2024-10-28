# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        final = []
        q= [root]
        while q:
            res = []
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                if  temp:
                    if temp.left:
                        q.append(temp.left)
                    else:
                        q.append(None)
                    
                    if temp.right:
                        q.append(temp.right)
                    else:
                        q.append(None)
                res.append(temp.val if temp else None)
            final.append(res)
        print(final)
        for a in final:
            if a != a[::-1]:
                return False
        return True
                    
                    

        
        