class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visit = [-1 for a in range(len(graph))]
        parent={}
        res=[True]
        def dfs(node,parent):

            if visit[node]<0:
                visit[node] = not parent[node][1]
                for a in graph[node]:
                    if visit[a] <0:
                        parent[a] = [node,visit[node]]
                        dfs(a,parent)
                    elif(a != parent[node][0]):
                        if visit[a]== visit[node]:
                            res[0] = False

           
        for index,a in enumerate(graph):
            if visit[index] <0:

                if a:
                    parent[index] = [-1,0]
                    dfs(index,parent)
                    if not res[0]:
                        return False
        return True
        