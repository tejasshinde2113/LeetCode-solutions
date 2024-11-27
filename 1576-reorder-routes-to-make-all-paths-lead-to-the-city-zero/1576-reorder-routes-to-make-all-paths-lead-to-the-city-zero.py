class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        d = dict()
        b= dict()

        for a in connections:
            if a[0] not in d:
                d[a[0]] = set()
            d[a[0]].add(a[1])
            if a[1] not in b:
                b[a[1]] = set()
            b[a[1]].add(a[0])
        
        cnt=[0]
        visited = set()



        def dfs(node,d,b,cnt):
            visited.add(node)

            for a in d.get(node,[]):
               if a not in visited:
                    cnt[0] += 1 
                    dfs(a, d, b, cnt)
            for a in b.get(node,[]):
                if a not in visited:
                    dfs(a, d, b, cnt)

        dfs(0,d,b,cnt)
        return cnt[0]
        