# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque([(root, 0,0)]) # node, level, xaxis
        res =[]
        dct =defaultdict(list)
        while q:

            for a in range(len(q)):
                temp,level,axis =q.popleft()

                dct[axis].append((level,temp.val))

                if temp.left:
                    q.append((temp.left,level+1,axis-1))
                if temp.right:
                    q.append((temp.right,level+1,axis+1))


        for k in range(min(dct.keys()),max(dct.keys())+1):
            l = sorted(dct[k])
            l = [a[1] for a in l]
            res.append(l)
        
        return res

                





        