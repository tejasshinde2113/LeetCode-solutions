# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        q=deque([[root,0]])
        res = []
        cnt = 0

        while q:
            
            temp,path = q.popleft()
            path ^= (1 << temp.val)

            if not temp.left and not temp.right:
                if path & (path-1) == 0:
                    cnt += 1
            
            if temp.left :
                q.append([temp.left, path ])
            if temp.right:
                q.append([temp.right, path ])
        
        return cnt

        