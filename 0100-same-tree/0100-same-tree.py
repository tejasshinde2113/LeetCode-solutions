# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def pre(root):
            res = []
            st=[]
            while root or st:
                while root:
                    res.append(root.val)
                    st.append(root)
                    root = root.left
                res.append(None)
                
                root = st.pop()
                root = (root.right)
            return res
        return pre(p) == pre(q)
        