# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        q1= deque([(p,0)])
        q2= deque([(q,0)])

        while q1 or q2:
            if len(q1) != len(q2):
                return False

            temp1,side1 = q1.popleft()
            temp2,side2 = q2.popleft()

            if temp1.val != temp2.val or side1 !=side2:
                return False
            
            if temp1.left:
                q1.append((temp1.left,0))

            if temp2.left:
                q2.append((temp2.left,0))

            if temp1.right:
                q1.append((temp1.right,1))

            if temp2.right:
                q2.append((temp2.right,1))
        
        if not q1 and not q2:
            return True
        else:
            return False