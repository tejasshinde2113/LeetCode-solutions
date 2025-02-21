# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if x==y:
            return False

        parent=[]
        depth = []


        q=deque([(root,None)])

        cnt = 0
        while q:
            for i in range(len(q)):
                node, par = q.popleft()

                if node.val == x or node.val==y:
                    parent.append(par.val if par else None)
                    depth.append(cnt)
                
                if len(parent)==2:
                    break
                
                if node.left:
                    q.append((node.left,node))
                if node.right:
                    q.append((node.right,node))
            cnt+=1
        print(parent,depth)
        if depth[0]==depth[1] and (parent[0]!=parent[1] and  parent[0] is not None):
            return True
        return False


        