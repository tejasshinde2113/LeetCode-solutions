# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = [root]

        def compare(temp, subroot):
            if temp and subroot:
                if temp.val != subroot.val:
                    return False
                return compare(temp.left,subroot.left) and compare(temp.right,subroot.right)
            elif not temp and not subroot:
                return True
            else:
                False

        while q:
            temp=q[0]
            del q[0]
            

            if compare(temp,subRoot):
                return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False
        