# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        q=[root]
        while q:
            for a in range(len(q)):
                temp = q[0]
                del q[0]
                if temp.val == val:
                    return temp
                
                elif temp.val > val:
                    if temp.left:
                        q.append(temp.left)
                else:
                    if temp.right:
                        q.append(temp.right)
        return None
        