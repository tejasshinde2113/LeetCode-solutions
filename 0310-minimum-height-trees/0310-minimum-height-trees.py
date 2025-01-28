class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adj =defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        edges = {}
        q=deque()
        for key,val in adj.items():
            if len(val) ==1:
                q.append(key)
            edges[key] = len(val)
        
        while q:
            if n<=2:
                return list(q)
            for a in range(len(q)):
                n-=1
                temp = q.popleft()
                for nn in adj[temp]:
                    edges[nn ] -=1
                    if edges[nn] == 1:
                        q.append(nn)
