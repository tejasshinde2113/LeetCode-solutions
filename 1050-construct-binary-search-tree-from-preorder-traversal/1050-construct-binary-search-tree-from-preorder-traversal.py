# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return
        

        res = TreeNode(preorder[0])
        mid = len(preorder)
        val = preorder[0]
        for i,a in enumerate(preorder):
            if a > val:
                mid = i
                break
        
        res.left = self.bstFromPreorder(preorder[1:mid])
        res.right = self.bstFromPreorder(preorder[mid:] if mid < len(preorder) else [])

        return res
        