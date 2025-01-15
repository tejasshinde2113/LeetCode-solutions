# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        cnt = 2
        add = TreeNode(val)
        q= deque([root])

        if depth == 1:
            add.left = root
            return add

        while q:
            for a in range(len(q)):
                temp = q.popleft()
                if cnt == depth:
                    if temp.left:
                        k = temp.left
                        temp.left = TreeNode(val)
                        temp2 = temp.left
                        temp2.left = k
                        temp2.right = None
                    else:
                        temp.left = TreeNode(val)
                    
                    if temp.right:
                        k = temp.right
                        temp.right = TreeNode(val)
                        temp2 = temp.right
                        temp2.right = k
                        temp2.left = None
                    else:
                        temp.right = TreeNode(val)
                    
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            cnt+=1
        return root

        