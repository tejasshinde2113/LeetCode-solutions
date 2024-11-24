# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = dict()
        temp =[]
        n= dict()
        for p,c,l in descriptions:
            if p not in d:
                d[p] = TreeNode(p)
            if c not in d:
                d[c] = TreeNode(c)
            
            if l:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
            temp.append(c)
        
        for a in d:
            if a not in temp:
                return d[a]
            
        
        

        