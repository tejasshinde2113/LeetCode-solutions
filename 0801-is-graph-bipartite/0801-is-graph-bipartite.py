class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visit = [-1 for a in range(len(graph))]
        parent={}
        def bfs(node):
            toggle =True
            q= [node]

            while q:
                temp = q[0]
                del q[0]

                visit[temp] = not parent[temp][1]
              

                for a in graph[temp]:
                    if visit[a] <0:
                        parent[a] = [temp, visit[temp]]
                        q.append(a)
                    elif(a != parent[temp][0]):
                        if visit[a]== visit[temp]:
                            return False

            return True
        for index,a in enumerate(graph):
            if visit[index] <0:

                if a:
                    parent[index] = [-1,0]
                    val = bfs(index)
                    if not val:
                        return False
        return True
        