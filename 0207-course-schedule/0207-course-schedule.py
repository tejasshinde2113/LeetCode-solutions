class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        visit = [0 for a in range(numCourses)]
        path = [0 for a in range(numCourses)]
        

        def dfs(root):
            visit[root] = 1
            path[root]=1
            for a in adj[root]:
                if not visit[a]:
                    if dfs(a):
                        return True
                elif path[a]==1:
                    return True
            path[root]=0
            return False
                    



        for a in range(numCourses):
            if not visit[a]:
                visit[a] = 1
                path[a]=1
                if dfs(a):
                    return False
        return True