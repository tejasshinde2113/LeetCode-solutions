# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1
        queue = deque([(root1, root2)])
        while queue:
            current_root1, current_root2 = queue.pop()
            if current_root1.left and current_root2.left: queue.append((current_root1.left, current_root2.left))
            elif not current_root1.left: current_root1.left = current_root2.left
            if current_root1.right and current_root2.right: queue.append((current_root1.right, current_root2.right))
            elif not current_root1.right: current_root1.right = current_root2.right
            current_root1.val += current_root2.val
        return root1
        if not root1: 
            return root2
        if not root2:
            return root1
        q=deque([(root1,root2)])
        while q:
            r1,r2 = q.pop()

            r1.val = r1.val+r2.val
            if r1.left and r2.left:
                q.append((r1.left,r2.left))
            elif not r1.left:
                r1.left = r2.left

            if r1.right and r2.right:
                q.append((r1.right,r2.right))
            elif not r1.right:
                r1.right = r2.right
            
        return root1



        