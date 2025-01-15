# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        visit = set()
        parent = dict()

        if k ==0:
            return [target.val]

        q= deque([root])
        while q:
            for a in range(len(q)):
                temp = q.popleft()

                if temp.left:
                    q.append(temp.left)
                    parent[temp.left] = temp
                if temp.right:
                    q.append(temp.right)
                    parent[temp.right] = temp
        
        visit.add(target)
        q = deque([target])
        cnt=0
        result =[]
        while q:
            for a in range(len(q)):
                temp = q.popleft()

                if temp.left and  temp.left not in visit:
                    q.append(temp.left)
                    visit.add(temp.left)
                if temp.right and temp.right not in visit:
                    q.append(temp.right)
                    visit.add(temp.right)
                
                if  temp in parent and  parent[temp] not in visit:
                    q.append(parent[temp])
                    visit.add(parent[temp])

            cnt+=1
            if cnt==k:
                break
        while q:
            node = q.popleft()
            result.append(node.val)
        
        return result
                  
            
        
        
        



                

        
        