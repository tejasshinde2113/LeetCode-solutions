# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        q=[root]
        while q:
            for a in range(len(q)):
                temp = q[0]
                del q[0]
            
                if temp.val > val:
                    
                    if temp.left:
                        q.append(temp.left)
                    else:
                        temp.left = TreeNode(val)
                        return root
                else:
                    if temp.right:
                        q.append(temp.right)
                    else:
                        temp.right = TreeNode(val)
                        return root
        