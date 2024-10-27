# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q=[root]
        while q:
            for a in range(len(q)):
                temp = q[0]
                temp1 = temp.right
                temp.right = temp.left
                temp.left = temp1
                del q[0]
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)

        return root
        