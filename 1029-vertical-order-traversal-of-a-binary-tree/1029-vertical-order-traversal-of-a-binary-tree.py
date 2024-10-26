# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[[root,0,0]]
     
        res=[]
        dct = dict()
        while q:


            for a in range(len(q)):
                temp2 = q[0][0]
                col2 = q[0][1]
                height = q[0][2]
                
                
                if temp2.right:
                    q.append([temp2.right,col2+1,height+1])   
                if temp2.left:
                    q.append([temp2.left,col2-1,height+1])             
                res.append([q[0][0].val,q[0][1],height])

                del q[0]

        res.sort(key=lambda x: (x[1],x[2],x[0]))
        for a in res:
            if a[1] not in dct:
                dct[a[1]] = []
            dct[a[1]].extend([a[0]])

        maxcol = max(dct.keys())
        mincol = min(dct.keys())


        final = []
        for a in range(mincol,maxcol+1):
            final.append(dct[a])


        return final

        