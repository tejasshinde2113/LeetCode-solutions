# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st=[]
        q=[]
        curr = root
        q.append(curr)
        if root is None:
            return [] 
        while q:
            length = len(q)
            res =[]
            for a in range(length):
                temp = q[0]
                del q[0]
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                res.append(temp.val)
            st.append(res)
        return st

        