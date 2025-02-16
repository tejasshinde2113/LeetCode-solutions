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
        final = root

        q = deque([root])

        while q:
            for i in range(len(q)):

                node  =q.popleft()
                templeft = node.left

                node.left = node.right
                node.right = templeft

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        return final
                
        