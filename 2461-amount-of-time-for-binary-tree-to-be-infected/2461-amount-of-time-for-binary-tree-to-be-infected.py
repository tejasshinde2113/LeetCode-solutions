# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root.left and not root.right:
            return 0
        temp = root

        q=deque([(root,None)])
        par ={}
        res = None
        while q:
            node,parent = q.popleft()
            if start == node.val:
                res = node


            par[node] = parent

            if node.left:
                q.append((node.left, node))

            if node.right:
                q.append((node.right,node))

        q=deque([res])
        s =set()
        cnt=0
        while q:
            cnt+=1
            for a in range(len(q)):
                node = q.popleft()
                s.add(node)

                if node.left and not node.left in s:
                    q.append(node.left)
                    s.add(node.left)
                
                if par[node] and not par[node] in s:
                    q.append(par[node])
                    s.add(par[node])

                if node.right and not node.right in s:
                    q.append(node.right)
                    s.add(node.right)
            
            
        return cnt-1
        
        

        