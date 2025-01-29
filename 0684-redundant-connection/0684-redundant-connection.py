class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q= deque()
        for a in range(1,len(indegree)):
            if indegree[a]==1:
                q.append(a)
        
        while q:
            temp = q.popleft()
            indegree[temp] -=1
        
            for a in adj[temp]:
                indegree[a]-=1
                if indegree[a]==1:
                    q.append(a)

        for u,v in edges[::-1]:
            if indegree[u]==2 and indegree[v]>0:
                return [u,v]
        