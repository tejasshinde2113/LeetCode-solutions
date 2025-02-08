# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = deque([( float('-inf'),root,float('inf'))]) # root, max , min

        while q:
            lower,temp,upper = q.popleft()

            if lower >= temp.val or upper <= temp.val:
                return False
            
            if temp.left:
                q.append((lower,temp.left,temp.val))
            if temp.right:
                q.append((temp.val,temp.right,upper))
        return True
        