class Solution:
    def soln(self,node,graph,lst,visited):
        visited[node]=0
        ans=1
        for i in graph[node]:
            if visited[i]==-1:
                ans&=self.soln(i,graph,lst,visited)
            else:
                ans&=visited[i]
        # print(node,ans)
        visited[node]=ans
        if ans==1:
            lst.append(node)
            return 1
        return 0


    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[-1]*n
        lst=[]
        for i in range(n):
            if visited[i]==-1:
                self.soln(i,graph,lst,visited)
        lst.sort()
        return lst