# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res =[]
        st=[]

        curr = root


        
        while curr or st:
            while curr:
                res.append(curr.val)
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            curr = curr.right
            
            
            
        return res
        