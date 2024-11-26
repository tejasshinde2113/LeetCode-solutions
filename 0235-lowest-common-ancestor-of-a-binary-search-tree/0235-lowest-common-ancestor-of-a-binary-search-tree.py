# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ss=[root]
        res = None
        while ss:
            for a in range(len(ss)):
                temp =ss[0]
                del ss[0]

                if temp.val < p.val and temp.val > q.val:
                    res = temp
                    break
                elif temp.val > p.val and temp.val < q.val:
                    res = temp
                    break
                elif temp.val == p.val or temp.val== q.val:
                    res = temp
                    break
                if temp.val < p.val and temp.val < q.val:
                    if temp.right:
                        ss.append(temp.right)
                if temp.val > p.val and temp.val > q.val:
                    if temp.left:
                        ss.append(temp.left)
        return res
        

        