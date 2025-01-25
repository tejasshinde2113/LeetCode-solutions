class Solution:
    def longestCycle(self, edges: List[int]) -> int:


        res = -1
        visit = [0 for a in range(len(edges))]
        
        def bfs(i):
            path = {}
            q = deque([[i,1]])
            while q:
                t,num= q.popleft()
                
                if edges[t] > -1:
                    
                    if edges[t] in path:
                        return num - path[edges[t]] +1
                    if visit[edges[t]] ==1:
                        return -1
                   
                    q.append([edges[t], num + 1])
                    path[t] = num
                    visit[t] = 1
                else:
                    return -1
            return -1


        for i,a in enumerate(visit):
            if edges[i] == -1:
                visit[i]=1
                continue
            if a==0:  
                temp = bfs(i)
                res = max(temp,res)
                
            
        return res 

        