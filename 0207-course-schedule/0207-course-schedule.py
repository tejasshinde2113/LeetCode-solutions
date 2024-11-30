class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        visit = [0 for a in range(numCourses)]
        path = [0 for a in range(numCourses)]


        def dfs(node,adj, visit,path):
            
            visit[node] = 1
            path[node] = 1
          
            for a in adj[node]:
                if not visit[a]:
                    if dfs(a,adj,visit,path) == True:
                        return True
                elif(path[a]==1):
                    return True
            path[node]=0
            return False

        for a in range(numCourses):
            if not visit[a]:
                if  dfs(a,adj,visit,path):
                    return False
        return True



        