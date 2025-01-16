# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        q=deque([root])
        check1= True

        if val > root.val:
            k = TreeNode(val)
            k.left = root
            return k
        while q:
            for a in range(len(q)):
                temp = q.popleft()

                if temp.val > val:
                    
                    
                    if temp.right:
                        if temp.right.val > val:
                            check1= False
                    
                    if check1:
                        l = temp.left
                        r = temp.right
                        new = TreeNode(val)
    
                        new.left = r
                        
                        temp.right = new
                        break
                    else:
                        check1 = True


                
                if temp.right:
                    q.append(temp.right)
        return root

        