class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        d={}
        for index, val in enumerate(isConnected):
            d[index+1]=[]
            for index2,v in enumerate(val):
                
                if v:
                    d[index+1].append(index2+1)
        
        visit=set()
        def bfs(node):
            q=[node]
            
            while q:
                n = q.pop()
                visit.add(n)
                for a in d[n]:
                    if a not in visit:
                        q.append(a)
                

        cnt=0
        for a in d:
            if a not in visit:
                bfs(a)
                cnt+=1
        return cnt
                    
        