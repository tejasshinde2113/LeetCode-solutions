# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []

        alphabet_dict = {i: chr(97 + i) for i in range(26)}

        if not root:
            return ''
        
        def dfs(root,path):
            if not root.left and not root.right:
                res.append(path)
            
            if root.left:
                dfs(root.left, alphabet_dict[root.left.val]+path)
            if root.right:
                dfs(root.right, alphabet_dict[root.right.val] + path)

            
        dfs(root,alphabet_dict[root.val])

        res.sort()

        return res[0]        